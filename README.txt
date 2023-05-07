# создаем виртуальное окружение
python -m venv venv

# активируем виртуальное окружение
venv\scripts\activate

# оюновляем пакетный менеджер
python -m pip install --upgrade pip

# устаналиваем фреймворк Django
pip install django

# создаем проект
django-admin startproject shop_project

# заходим в папку shop_project
cd shop_project

# создаем приложение 
python manage.py startapp shop

# подключаем базу данных
python manage.py migrate 

# запуск сервера
python manage.py runserver

# при изменении структуры базы данных
python manage.py makemigrations
python manage.py migrate 

# регистрируем админестратора
python manage.py createsuperuser
name : Alex
Email : alex@jan.de 
Password : 456.de!43