# blog_sayt
Kodni ishlatish uchun qilinadigan amallar

cmd ni ochib olamiz

git clone https://github.com/Aslbekjon/blog_sayt.git

#for windows

cd blog_sayt

python -m venv venv

.\venv\Scripts\activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

