all: runserver

runserver: 
	PYTHONPATH=$PYTHONPATH:. python manage.py runserver --settings=settings
