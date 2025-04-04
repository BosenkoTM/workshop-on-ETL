
# Бизнес-кейс «StockSense»

Самостоятельная работа

6.1.1. Развернуть ВМ [ubuntu_mgpu.ova](https://disk.yandex.ru/d/Psofa9xtbgUEOw) в [VirtualBox](https://disk.yandex.ru/d/3fD00plnL_a4Cw).

6.1.2. Клонировать на ПК задание **Бизнес-кейс «StockSense»** в домашний каталог ВМ. 

`git clone https://github.com/BosenkoTM/workshop-on-ETL.git`

6.1.3. Запустить контейнер с **Бизнес-кейсом «StockSense»**, изучить  основные элементы `DAG` в `Apache Airflow`. 
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

6.1.5. Спроектировать верхнеуровневую архитектуру аналитического решения **Бизнес-кейса «StockSense»** в `draw.io`. Необходимо использовать:
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
- ERD-схема базы данных Postgre SQL;
- SQL-запросы, позволяющие проверить наличие выгруженных агрегированных данных бизнес-задачи. 

После проверки преподавателем работоспособности `DAG`, выгрузить отчет на портал [moodle]().


## Этапы запуска среды

1. **Остановка всех контейнеров Docker**  

   ```bash
   sudo docker stop $(sudo docker ps -a -q)
   ```

2. **Удаление всех контейнеров Docker**  
   ```bash
   sudo docker rm -f $(sudo docker ps -a -q)
   ```

3. **Удаление всех образов Docker**  
   ```bash
   sudo docker rmi -f $(sudo docker images -q)
   ```

4. **Создание нового Docker образа**  
   Эта команда строит новый Docker образ с именем `custom-airflow:slim-2.8.1-python3.11` на основе текущего контекста:
   ```bash
   sudo docker build -t custom-airflow:slim-2.8.1-python3.11 .
   ```

5. **Запуск среды с помощью Docker Compose**  

   ```bash
   sudo docker compose up --build
   ```

Веб-сервер инициализирует несколько задач, поэтому подождите несколько секунд, после чего сможете получить доступ к веб-серверу Airflow по адресу http://localhost:8080.

Чтобы остановить выполнение примеров, выполните следующую команду:

Для версии `v2`:

```bash
docker compose down -v
```

## Подключение к PostgreSQL через DBeaver для просмотра таблицы

1. **Убедитесь, что контейнер PostgreSQL работает**

   Перед подключением убедитесь, что ваш контейнер с PostgreSQL работает. Он настроен с использованием порта `5433`, что означает, что база данных будет доступна через этот порт на вашем локальном хосте.

2. **Запуск DBeaver**

   Если у вас еще нет DBeaver, скачайте и установите его с официального сайта: [DBeaver.io](https://dbeaver.io/).

3. **Создание нового подключения в DBeaver**

   После запуска DBeaver, выполните следующие шаги:

   - Откройте DBeaver.
   - Перейдите в меню **Database** > **New Database Connection**.
   - В поле поиска выберите **PostgreSQL** и нажмите **Next**.

4. **Настройка подключения**

   В появившемся окне заполните поля:

   - **Host**: `localhost` (или `127.0.0.1`).
   - **Port**: `5433` (порт, проброшенный в `docker-compose.yml`).
   - **Database**: `airflow` (это имя базы данных, как указано в `docker-compose.yml`).
   - **Username**: `airflow` (пользователь, указанный в `docker-compose.yml`).
   - **Password**: `airflow` (пароль, указанный в `docker-compose.yml`).

   Затем нажмите **Test Connection**, чтобы убедиться, что DBeaver может подключиться к базе данных.

5. **Подключение к базе данных**

   Если тест прошел успешно, нажмите **Finish** для завершения настройки подключения.

6. **Просмотр данных в таблице**

   - В левой панели DBeaver найдите подключение, которое вы только что создали (обычно оно будет отображаться с именем **airflow**).
   - Разверните подключение, перейдите в раздел **Schemas** > **public** > **Tables**.
   - Найдите таблицу **pageview_counts** (она была создана с помощью скрипта `create_table.sql`, загруженного в контейнер).
   - Щелкните правой кнопкой мыши на таблице **pageview_counts** и выберите **View Data** > **All Rows** для просмотра содержимого таблицы.

7. **Дополнительные действия**

   - Вы можете выполнять SQL-запросы через вкладку **SQL Editor**, например, для извлечения специфичных данных, агрегации или анализа.



## Индивидуальные задания

[Лабораторная работа 6.1 Разработка полного ETL-процесса. Оркестровка конвейера данных](http://95.31.0.249/moodle/mod/assign/view.php?id=748)


