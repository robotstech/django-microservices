#!/bin/bash

sleep 10
python manage.py collectstatic --noinput
python manage.py migrate
echo "from django.contrib.auth import get_user_model;su = get_user_model().objects.create_superuser('admin', 'admin@messageboards.com', 'T@stpassword1') if not get_user_model().objects.filter(username='admin').exists() else None" | python manage.py shell

echo "Running command '$*'"
exec /bin/bash -c "$*"