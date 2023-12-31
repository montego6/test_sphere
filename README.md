## Тестовое задание для компании Сфера

## Задание
Требуется реализовать бекенд для приложения пропуска автомобилей на охраняемую территорию.
Для администраторов нужна админ панель с таблицами, в которые они смогут добавлять пользователей-охранников и информацию о машинах, которым разрешен въезд.
Также необходимо реализовать GraphQL API для отрисовки информации о всех имеющихся автомобилях для будущих нужд фронтенда.

## Решение
В решении использованы Django, graphene-django, DjangoRestFramework. Созданы модели для пропуска машин, для пользователей расширена модель AbstractUser. Для GraphQL API создана схема и мутации, позволяющие выполнять все CRUD-операции. Использованы сериализаторы из DRF, если нужна будет в дальнейшем какая-то валидация. 

## API
**/graphql** 
Модель carPass. Поля, которые можно запросить: id, uuid, brand, model, plate_number, owners_name, created_ad, updated_at.
Мутации для create, update, delete: createCar, updateCar, deleteCar

## Запус приложения

### Запуск приложения с помощью Docker
В корне проекта создайте **.env** файл и пропишите в нем следующие переменные:
```
DB_NAME=app
DB_USER=postgres
DB_PASSWORD=supersecretpassword
DB_HOST=db
DB_PORT=5432
```
Затем мы запускаем приложение следующей Docker командой в терминале:
```
docker-compose up -d
```
Приложение запуститься и должно быть доступно по локальному адресу [127.0.0.1:8000](http://127.0.0.1:8000)

Остановить приложение/запустить заново:
```
docker-compose stop
docker-compose start
```
Остановить приложение и удалить все связанные контейнеры, включая базу данных:
```
docker-compose down -v
```
При изменениях в коде проекта, необходимо заново создать образ и запустить сервисы:
```
docker-compose build
docker-compose up -d
```

### Запуск приложения без использования Docker
Сначала установим pipenv и активируем его:
```
pip install pipenv
pipenv shell
```
Затем установим все зависимости проекта, отдав следующую команду:
```
pipenv install
```
После этого в корне проекта создайте **.env** файл и пропишите в нем следующие переменные:
```
DB_NAME= название вашей базы данных
DB_USER= имя пользователя
DB_PASSWORD= пароль пользователя
DB_HOST=localhost
DB_PORT=5432
```
***Убедитесь, что PostgreSQL запущен на локальной машине и принимает соединения на порту 5432***

Затем в корне проекта отдаем следующие команды, применяя миграции к базе данных:
```
python3 manage.py migrate
```
После этого можно запускать сервер следующей командой:
```
python3 manage.py runserver
```
Приложение запуститься и должно быть доступно по локальному адресу [127.0.0.1:8000](http://127.0.0.1:8000)