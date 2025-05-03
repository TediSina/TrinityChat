python3.12 -m pip install -r requirements.txt
python3.12 manage.py tailwind install
python3.12 manage.py tailwind build
python3.12 manage.py collectstatic --noinput
