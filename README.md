python3 -m venv env

source env/bin/activate

pip install django

django-admin startproject watchmate

cd watchmate

python3 manage.py startapp watchlist_app

python3 manage.py  makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser

pip install djangorestframework

python3 manage.py runserver 8069


----------------------------------------------

![image](https://github.com/user-attachments/assets/a89f8334-ae40-4049-9f78-07a0362f94a9)

![image](https://github.com/user-attachments/assets/6f7d7883-0a00-4dd7-bd59-4414d63bfdf9)






