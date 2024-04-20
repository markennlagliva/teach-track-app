rm -f "db.sqlite3"

python3 manage.py makemigrations
python3 manage.py migrate

echo "from teachtrack_auth.models import CustomUser; CustomUser.objects.create_superuser('markenn', 'markenn@gmail.com', 'markenn')" | python3 manage.py shell