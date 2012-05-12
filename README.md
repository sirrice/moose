# What

Moose is an app that lets people send anonymous feedback to other.  The key application is use during talks so that participants can anonymously send feedback to the presenter.


# To Run

    make runserver


# To push to AWS

Make sure threemooseketeers.pem is in ~/.ssh/

    make deploy

## What's actually happening

    ssh -i threemooseketeers.pem ubuntu@ec2-107-21-158-48.compute-1.amazonaws.com  
    sudo su - django  
    cd moose  
    git pull  
    exit  
    sudo service moose stop  
    sudo service moose start  

# To get it working on AWS

    sudo apt-get update  
    sudo apt-get install postgresql python-pip git nginx build-essential python-psycopg2 python-dev emacs  
    sudo pip install Django==1.4 uwsgi  
    sudo adduser django  
    	
    sudo su - django  
    git clone git://github.com/sirrice/moose.git  
    cd moose  

--> generate  private_settings.py from private_settings.template  

(back as the root user)  

    sudo cp wsgi/nginx/nginx.conf /etc/nginx/  
    sudo cp wsgi/upstart/moose.conf /etc/init/  
    sudo initctl reload-configuration  
    sudo service nginx start  
    sudo service moose start  