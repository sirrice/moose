all: runserver

runserver:
	PYTHONPATH=$PYTHONPATH:. python manage.py runserver --settings=settings

syncdb:
	PYTHONPATH=$PYTHONPATH:. python manage.py syncdb --settings=settings