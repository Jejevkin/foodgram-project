# foodgram-project — сайт «Продуктовый помощник». 
Это онлайн-сервис, где пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

## Подготовка к работе:

Клонируйте репозиторий на локальную машину.
```
git clone https://github.com/Jejevkin/foodgram-project.git
```
Создайте файл .env и заполните его своими значениями. Все нужные переменные и их примерные значения описаны файле .env.template.

Для получения SSL-сертификатов откройте `letsencrypt.sh` и впишите:

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

Запустите процесс сборки и запуска контейнеров:
```
docker-compose up
```
Чтобы применить миграции, введите:
```
docker-compose -f docker-compose.yaml exec web python manage.py migrate --noinput
```
Для создания суперпользователя, необходимо ввести:
```
docker-compose -f docker-compose.yaml exec web python manage.py createsuperuser
```
Чтобы добавить в базу ингредиенты и теги:
```
docker-compose -f docker-compose.yaml exec web python manage.py load_ingredients_data
```
Остановить работу можно командой:
```
docker-compose stop
```

## Технологии

* [Django](https://www.djangoproject.com/) - фреймворк для веб-приложений;
* [PostgreSQL](https://www.postgresql.org/) - объектно-реляционная система управления базами данных;
* [Docker](https://www.docker.com/) - ПО для автоматизации развёртывания и управления приложениями в средах с поддержкой контейнеризации;
* [Docker-Compose](https://docs.docker.com/compose/) - инструмент для создания и запуска многоконтейнерных Docker приложений. 
