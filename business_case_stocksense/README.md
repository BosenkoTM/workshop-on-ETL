
# Бизнес-кейс «StockSense»

Самостоятельная работа

6.1.1. Развернуть ВМ [ubuntu_mgpu.ova](https://disk.yandex.ru/d/Psofa9xtbgUEOw) в [VirtualBox](https://disk.yandex.ru/d/3fD00plnL_a4Cw).

6.1.2. Клонировать на ПК задание **Бизнес-кейс «StockSense»** в домашний каталог ВМ. 

`git clone https://github.com/BosenkoTM/workshop-on-ETL.git`

6.1.3. Запустить контейнер с кейсом, изучить  основные элементы `DAG` в `Apache Airflow`. 
   - Создать `DAG` согласно алгоритму, который предоставит преподаватель.
   - Изучить логи, выполненного DAG. Скачать логи из контейнера в основную ОС.

Пример `docker-compose.yml` создает базу данных в Postgres:

- Host: `localhost`
- Port: `5433`
- Username: `airflow`
- Password: `airflow`
- Database: `airflow`

Эта база данных инициализируется таблицей `pageview_counts`.

**6.1.4.** Агрегированные данные бизнес-процесса, полученные в результате работы `DAG` в `Apache Airflow`, выгрузить в `Postgr SQL`. 

6.1.5. Спроектировать верхнеуровневую архитектуру аналитического решения задания **Бизнес-кейса «StockSense»** в `draw.io`. Необходимо использовать:
   - `Source Layer` - слой источников данных.
   - `Storage Layer` - слой хранения данных.
   - `Business Layer` - слой для доступа к данным пользователей.

6.1.6. Спроектировать архитектуру `DAG` **Бизнес-кейса «StockSense»** в `draw.io`. Необходимо использовать:
   - `Source Layer` - слой источников данных.
   - `Storage Layer` - слой хранения данных.
   - `Business Layer` - слой для доступа к данным пользователей.

6.1.7. Построить диаграмму Ганта работы `DAG` в `Apache Airflow`.

6.1.8. Результаты исследований представить в виде файла `ФИО-06.pdf`, в котором отражены следующие результаты:
- постановка задачи;
- исходный код всех DAGs, которые требовались для решения задачи, а также представить граф `DAG` в `Apache Airflow`;
- верхнеуровневая архитектура задания **Бизнес-кейса «StockSense»**, выполненная в `draw.io`;
- архитектура `DAG` **Бизнес-кейса «StockSense»** , выполненная в `draw.io`;
- диаграмма Ганта `DAG` в `Apache Airflow`;
- ERD-схема базы данных Postgr SQL;
- SQL-запросы, позволяющие проверить наличие выгруженных агрегированных данных бизнес-задачи. 

После проверки преподавателем работоспособности `DAG`, выгрузить отчет на портал [moodle]().


## Использование

Чтобы начать работу с примерами кода, запустите `Airflow` с помощью `Docker Compose`, выполнив команду:

Для версии `v1`:

```bash
docker-compose up -d
```
Для версии `v2`:

```bash
docker compose up -d
```

Веб-сервер инициализирует несколько задач, поэтому подождите несколько секунд, после чего сможете получить доступ к веб-серверу Airflow по адресу http://localhost:8080.

Чтобы остановить выполнение примеров, выполните следующую команду:

Для версии `v1`:

```bash
docker-compose down -v
```
Для версии `v2`:

```bash
docker compose down -v
```

## Usage

To get started with the code examples, start Airflow with Docker Compose with the following command:

```bash
docker-compose up -d
```

The webserver initializes a few things, so wait for a few seconds, and you should be able to access the
Airflow webserver at http://localhost:8080.

To stop running the examples, run the following command:

```bash
docker-compose down -v
```
