define DEPLOY_CMD
cd /home/django/moose; sudo -u django git pull; sudo service moose stop; sudo service moose start;
endef

all: runserver

runserver:
	PYTHONPATH=$PYTHONPATH:. python manage.py runserver --settings=settings

syncdb:
	PYTHONPATH=$PYTHONPATH:. python manage.py syncdb --settings=settings

deploy:
	ssh -f -i ~/.ssh/threemooseketeers.pem ubuntu@ec2-107-21-158-48.compute-1.amazonaws.com "$(DEPLOY_CMD)"
