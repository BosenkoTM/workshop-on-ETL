### Раздел 1/ Основы ETL и Архитектура данных
1.  В чем суть процессов **ETL** и **ELT**, и чем они отличаются от **Data Sourcing**?
2.  Как устроена **архитектура слоев данных** (Source, Staging, Storage/DWH, Business Layer) и зачем нужен каждый слой?
3.  Что такое **Data Warehouse**, **Data Lake** и **Data Mart**? В чем их ключевые различия?
4.  Какие форматы данных используются в инженерии данных (**CSV, JSON, Parquet**) и в чем преимущество Parquet для больших данных?
5.  Что такое **нормализация** БД, **идемпотентность** операций и **Data Lineage**?

### Раздел 2. Pentaho Data Integration (PDI)
6.  Какие основные инструменты входят в пакет Pentaho (**Spoon, Pan, Kitchen**) и для чего служит каждый из них?
7.  В чем разница между **трансформацией** (`.ktr`) и **заданием** (`.kjb`), и как они связаны?
8.  Как работают ключевые шаги трансформации: **Filter Rows**, **Select Values**, **Calculator**, **Sort Rows**, **Value Mapper**?
9.  В чем разница между способами объединения данных: **Merge Join**, **Stream Lookup** и **Append Streams**?
10. Как настроить подключение к базе данных (использование **JDBC**) и работу с переменными в PDI?

### Раздел 3. Apache Airflow и Оркестрация
11. Из каких основных компонентов состоит архитектура Airflow (**Scheduler, Webserver, Worker, Metadata DB**)?
12. Что такое **DAG**, как задается расписание (**Cron expression**) и что такое **DAG Run**?
13. Какие типы операторов существуют (**BashOperator, PythonOperator, Sensor**) и для чего они нужны?
14. Что такое механизмы **XCom**, **Backfill**, **Catchup** и **SLA** в контексте Airflow?
15. Как управлять зависимостями задач (оператор `>>`) и обрабатывать ветвления (**BranchPythonOperator**)?

### Раздел 4. Docker и Виртуализация
16. В чем разница между **образом** (Image), **контейнером** (Container) и **виртуальной машиной**?
17. Как использовать основные команды Docker CLI: `run`, `ps`, `images`, `build`, `pull`, `stop`, `rm`, `system prune`, `exec`, `cp`?
18. Для чего нужен файл **Dockerfile** (инструкции `FROM`, `RUN`, `CMD`, `EXPOSE`)?
19. Что такое **Docker Compose**, структура файла `docker-compose.yml` (ports, volumes, services) и команды управления им?
20. Что такое **Docker Volume** и зачем он нужен для баз данных?

### Раздел 5. Python (Pandas, Dask) и Разработка
21. Какие основные функции библиотеки **Pandas** используются для ETL (`read_csv`, `fillna`, `dropna`, `groupby`, `merge`, `to_csv`)?
22. В чем главное преимущество **Dask** перед Pandas, что такое «ленивые вычисления» и зачем нужны методы `.compute()`, `.persist()` и `.visualize()`?
23. Как управлять зависимостями в Python (**pip**, `requirements.txt`, виртуальные окружения **venv**)?
24. Что такое **Unit-тестирование**, **Integration Testing**, **Mocking** и принцип **DRY**?
25. Какие библиотеки используются для работы с API (**Requests**), базами данных (**psycopg2**, **SQLAlchemy**) и AWS (**boto3**)?

### Раздел 6. SQL и Базы Данных
26. Чем отличаются реляционные БД (**PostgreSQL, MySQL**) от NoSQL (**MongoDB**)?
27. Как работают операторы выборки и фильтрации: **SELECT**, **DISTINCT**, **WHERE**, **LIKE**, **BETWEEN**, **IN**, **LIMIT**?
28. Как работают агрегация и группировка: **GROUP BY**, **HAVING**, агрегатные функции (`COUNT`, `SUM`, `AVG`)?
29. Как изменять данные и структуру: **INSERT**, **UPDATE**, **DELETE**, **DROP**, **CREATE TABLE**?
30. Какие типы соединений таблиц (**JOIN**: Inner, Left, Right, Full) и объединения запросов (**UNION**) существуют?

### Раздел 7. Облачные технологии (AWS) и DevOps 
*   Какие функции выполняют сервисы AWS: **S3, EC2, RDS, Lambda, Glue, Redshift, IAM, CloudWatch**?
*   Что такое **CI/CD**, **DevOps**, **IaC** и как работает **Git** (`clone`, `pull`, `push`, `branch`)?