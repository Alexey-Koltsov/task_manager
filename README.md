# Проект: task_manager
Описание проекта: CRUD операции для управления задачами (create, get, get_list,
update, delete), где модель задачи состоит из uuid, названия, описания, 
статусов: создано, в работе, завершено.

Общая схема работы:

1. Пользователь отправляет запрос к FastAPI.
2. На FastAPI реализованы CRUD операции:
   1. create - создать задачу,
   2. get - получить задачу по uuid,
   3. get_list - получить все задачи,
   4. update - изменить задачу по uuid,
   5. delete - удалить задачу по uuid.

## Как развернуть проект

## 1. Клонировать проект с GitHub
```commandline
git@github.com:Alexey-Koltsov/task_manager.git
```

## 2. Перейти в директорию проекта
```commandline
cd microservices
```

## 3. Создать в корне проекта файл .env с данными
```commandline
ENV=production
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_HOST=db_host
POSTGRES_PORT=5432
POSTGRES_DB=db
```

## 4. Поднимаем сеть контейнеров

В новом окне терминала перейти в корневую директорию проекта, где находится
файл docker-compose.yaml, и ввести в командной строке
```commandline
docker-compose up --build
```

В процессе сбора контейнера fastapi происходит создание создание таблиц
категории и задача. Для категории создаются две записи:
```commandline
id=1
name='овощи'
```
и
```commandline
id=2
name='фрукты'
```

## 5. Переходим по адресу к эндпоинтам FastAPI и создаем задачы в базе данных Postgres
```commandline
http://127.0.0.1:9000/docs#/
```

## 6. Переходим по адресу к эндпоинтам DjangoAPI и запрашиваем задачы по их id
```commandline
http://127.0.0.1:8000/swagger/
```
