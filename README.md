
# foodgram-project — [«Продуктовый помощник»](https://foodgram-project.site/)

Дипломный проект программы Яндекс.Практикум [Python-разработчик](https://praktikum.yandex.ru/backend-developer/)

Это онлайн-сервис, где пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

## Подготовка к работе:

1. Клонируйте репозиторий на локальную машину.
  ```
  git clone https://github.com/Jejevkin/foodgram-project.git
  ```
2. Создайте файл .env и заполните его своими значениями. Все нужные переменные и их примерные значения описаны файле .env.template.
====

3. Для получения SSL-сертификатов откройте `letsencrypt.sh` и впишите:

  - вместо `example.com` свои домены через пробел;
  - email;
  - поменяйте пути, если меняли их в папке.

  Затем запустите:
  ```
  chmod +x letsencrypt.sh
  ```
  и 
  ```
  ./letsencrypt.sh
  ```
  Выполнив последнюю команду, появится `data` с сертификатами необходимые для работы `nginx` и `certbot`.
  ====

4. Запустите процесс сборки и запуска контейнеров:
  ```
  docker-compose up
  ```
5. Чтобы применить миграции, введите:
  ```
  docker-compose -f docker-compose.yaml exec web python manage.py migrate --noinput
  ```
6. Для создания суперпользователя, необходимо ввести:
  ```
  docker-compose -f docker-compose.yaml exec web python manage.py createsuperuser
  ```
7. Чтобы добавить в базу ингредиенты и теги:
  ```
  docker-compose -f docker-compose.yaml exec web python manage.py load_ingredients_data
  ```
8. Остановить работу можно командой:
  ```
  docker-compose stop
  ```

## Технологии
* [Python](https://www.python.org/) - высокоуровневый язык программирования общего назначения;
* [Django](https://www.djangoproject.com/) - фреймворк для веб-приложений;
* [Django REST framework](https://www.django-rest-framework.org/) - API фреймворк для Django;
* [PostgreSQL](https://www.postgresql.org/) - объектно-реляционная система управления базами данных;
* [Nginx](https://nginx.org/) - HTTP-сервер и обратный прокси-сервер, почтовый прокси-сервер, а также TCP/UDP прокси-сервер общего назначения;
* [Certbot](https://certbot.eff.org/) - программный инструмент для автоматического использования сертификатов [Let’s Encrypt](https://letsencrypt.org/);
* [Sentry](https://sentry.io/) - приложение, встраиваемое в Django для оперативного мониторинга ошибок;
* [Docker](https://www.docker.com/) - ПО для автоматизации развёртывания и управления приложениями в средах с поддержкой контейнеризации;
* [Docker-Compose](https://docs.docker.com/compose/) - инструмент для создания и запуска многоконтейнерных Docker приложений. 
