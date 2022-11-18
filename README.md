# Проект: 
Yamdb_Final (Яндекс.Практикум)

> **Для этого проекта реализовано автоматический запуск тестов, обновление образов на Docker Hub, автоматический деплой на боевой сервер при пуше в главную ветку master.**

> **Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен администратором (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
В каждой категории есть произведения: книги, фильмы или музыка. 
Произведению может быть присвоен жанр (Genre) из списка предустановленных. Новые жанры может создавать только администратор.
Пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.**
___

## **Стек технологий**
![CI](https://img.shields.io/badge/Django%20Rest%20Framework-3.12.4-success)
![CI](https://img.shields.io/badge/Django-2.2.16-green)
![CI](https://img.shields.io/badge/Requests-2.26.0-yellow)
![CI](https://img.shields.io/badge/Simple--JWT-5.2.0-ff69b4)
![CI](https://img.shields.io/badge/Python-v3.8-blue)
![CI](https://img.shields.io/badge/-Docker-red)
![CI](https://img.shields.io/badge/-Docker--compose-orange)
## **Стек технологий**
**Запуск проекта:**

**Клонировать репозиторий [
Yamdb_Final](https://github.com/Aleksandr-Meshkov/Yamdb_Final) и перейти в него в командной строке:**

- ```cd 
Yamdb_Final```

**Шаблон наполнения env-файла:**

 - ```DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql```
 - ```DB_NAME=postgres # имя базы данных```
 - ```POSTGRES_USER=postgres # логин для подключения к базе данных```
 - ```POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)```
 - ```DB_HOST=db # название сервиса (контейнера)```
 - ```DB_PORT=5432 # порт для подключения к БД```

**Команды для первого запуска:**

  - ```docker-compose up``` - ***Cоздание сборки контейнеров***

  - ```docker-compose exec web python manage.py migrate``` - ***Выполнить миграции:***

  - ```docker-compose exec web python manage.py createsuperuser``` - ***Создать суперпользоателя***

  - ```docker-compose exec web python manage.py collectstatic --no-input``` - ***Собрать статику***

**Загрузить дамп базы**

  - ```docker-compose exec web python manage. py loaddata fixtures.json```
___

**Авторы проекта:**

**https://github.com/Aleksandr-Meshkov**

**Документация:**

**http://127.0.0.1/redoc/**<br>
**https://www.django-rest-framework.org/**<br>
**https://www.djangoproject.com/**<br>
**https://django-rest-framework-simplejwt.readthedocs.io/en/latest/**

![CI](https://github.com/Aleksandr-Meshkov/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
