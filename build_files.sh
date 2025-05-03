pip3.12 install -r requirements.txt
python3.12 manage.py tailwind install
python3.12 manage.py migrate
python3.12 manage.py tailwind build
python3.12 manage.py collectstatic --noinput
