<h2 align="center">Хабы</h2>


### Описание проекта:
Веб-приложение Парсер статей.

Функционал:
- Парсинг хабов на статьи каждые 10 минут (заголовок, дата, ссылка на пост, имя автор, ссылка на автора)
- Админ панель для добавления статей, хабов
- Хранение статей и хабов в базе данных

### Инструменты разработки

**Стек:**
- Python >= 3.11
- Django == 5.0.3
- Celery
- Redis
- PostgreSQL
- Docker


## Разработка

##### 1) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 2) Установить poetry на компьютер

    https://python-poetry.org/docs/#installation

##### 3) Активировать виртуальное окружение и установить зависимости

        poetry install

##### 4) Переименовать файл .env.example на .env и изменить SECRET_KEY (другие данные если есть необходимость)

##### 5) Установить docker на свою ОС

##### 6) Запустить контейнеры с сервисами через docker

    docker compose up -d

##### 7) Произойдёт инициализация celery, а именно процессов: worker, beat, flower 

##### 8) Автоматически создастся супер пользователь и три Hubs для начального парсинга

##### 9) Админ панель Django для работы с БД, учётные данные (admin/admin)
        
    http://localhost:8001/admin/
    



