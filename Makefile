isort:
	isort .

check-style:
	flake8

###########################
### MANAGEMENT COMMANDS ###
###########################

runserver:
	python django_tutorial/manage.py runserver

migrate:
	python django_tutorial/manage.py migrate

polls-make-migration:
	python django_tutorial/manage.py makemigrations polls

create-superuser:
	python django_tutorial/manage.py createsuperuser

shell:
	python django_tutorial/manage.py shell_plus --print-sql
