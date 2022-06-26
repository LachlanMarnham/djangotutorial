runserver:
	python django_tutorial/manage.py runserver

isort:
	isort .

check-style:
	flake8
