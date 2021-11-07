export SECRET_KEY='choomba'
export WTF_CSRF_SECRET_KEY='powerful secret key'
export MAIL_USERNAME='gavin.kariuki@student.moringaschool.com'


python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py server --port 8888