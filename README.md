Техзадание - Создать БД по заданной архитектуре данных используя миграции
Django / Flask (UML - диаграмма)

- Используйте DB seeder для Django ORM / Flask-SQLAlchemy для
заполнения базы данных.
- Построить простейшее взаимодействие с БД (Запись, удаление,
получение и т.д.) (Хотя бы эти 3 минимум)
- Описать для основных элементов (на свой взгляд) тэги для
фильтрации данных
- Построить API для взаимодействия с описанными выше механизмами


## Инструменты

- Python 3.9
- Django
- DjangoRestFramework
- drf-spectacular for swagger
- Postgresql 


------------------------------------------------

## Старт
- скачать проект с репозитория
- установить зависимости requirements.txt командой: pip install -r requirements.txt 
- Внести в файл .env данные бд
- Произвести миграции командами - 'python manage.py makemigrations', 'python manage.py migrate'
- Внести первоначальные данные в бд, для этого указать данные в seeds.py(по умолчанию внесутся в рандомном порядке)
- Также можно внести первоначальные данные в бд через админ панель предварительно создав пользователя 
- Запустить проект

#### Запустить сервер

- Запуск свагера: 'адрес вашего хоста:'/api/docs/ (в файле shema.py для примера описан метод с одной моделью)
- Остальные маршруты указаны в urls.py папки проекта

#### Дополнительно
- примеры фильтрации указаны в файле views.py
- также прописаны параметры для админ-панели(встроенная Django) можно использовать
- шаблоны не подключались
- локальные настройки не использовались  