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
