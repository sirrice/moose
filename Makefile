all: runserver

runserver: 
	export PYTHONPATH=$PYTHONPATH:.
	python manage.py runserver --settings=settings
