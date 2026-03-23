import json
import pathlib
import airflow.utils.dates
import requests
import requests.exceptions as requests_exceptions
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

# Базовая директория для сохранения данных (проброшена из Docker)
DATA_DIR = "/opt/airflow/data"
JSON_FILE = f"{DATA_DIR}/launches.json"
IMAGES_DIR = f"{DATA_DIR}/images"

dag = DAG(
    dag_id="download_rocket_launch",
    description="Download rocket pictures of recently launched rockets.",
    start_date=airflow.utils.dates.days_ago(14),
    schedule_interval="@daily",
    catchup=False
)

# Скачиваем JSON в проброшенную папку data
download_launches = BashOperator(
    task_id="download_launches",
    bash_command=f"curl -o {JSON_FILE} -L 'https://ll.thespacedevs.com/2.0.0/launch/upcoming'",
    dag=dag,
)

def _get_pictures():
    # Убеждаемся, что директория существует
    pathlib.Path(IMAGES_DIR).mkdir(parents=True, exist_ok=True)

    # Загружаем все изображения
    with open(JSON_FILE) as f:
        launches = json.load(f)
        image_urls = [launch["image"] for launch in launches.get("results", []) if launch.get("image")]
        
        for image_url in image_urls:
            try:
                response = requests.get(image_url)
                image_filename = image_url.split("/")[-1]
                target_file = f"{IMAGES_DIR}/{image_filename}"
                with open(target_file, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded {image_url} to {target_file}")
            except requests_exceptions.MissingSchema:
                print(f"{image_url} appears to be an invalid URL.")
            except requests_exceptions.ConnectionError:
                print(f"Could not connect to {image_url}.")

get_pictures = PythonOperator(
    task_id="get_pictures", 
    python_callable=_get_pictures, 
    dag=dag
)

notify = BashOperator(
    task_id="notify",
    bash_command=f'echo "There are now $(ls {IMAGES_DIR}/ | wc -l) images in {IMAGES_DIR}."',
    dag=dag,
)

download_launches >> get_pictures >> notify