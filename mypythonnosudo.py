#!/usr/bin/python
import os
def install_django():
	print('installing django')
install_django()
def install_pip():
	os.system('yum -y install python-pip')
	print('installing python-pip')
install_pip()
def install_virtualenv():
	os.system('cd /opt')
	os.system('pip install virtualenv')
	os.system('virtualenv django-env')
	print('installing virtual-env')
install_virtualenv()
# This is activating the django
def activate_virtualenv():
	os.system('source /opt/django/django-env/bin/activate')
	os.system('which python')
	os.system('pip install django')
        os.system('django-admin --version')
        os.system('django-admin startproject project1; exists_ok=true')
	os.system('tree project1')
        print('installing tree')
	print('installing django')
	os.system('python /opt/django/project1/ manage.py runserver 0.0.0.0:8000&')
	print('done')
activate_virtualenv()
# installing git
import os
def install_git():
	print('installing git')
	os.system('yum -y install git')
	os.system('git clone https://github.com/fjemal/NTI-300-repository')
install_git()
import os
def install(package):
	print('installing package')
	os.system('yum -y install '+package)
install('tree')
def mailx():
	print('installing mailx')
	os.system('yum -y install mailx')
mailx()
def kernel():
	print('installing kernel')
	os.system('yum -y clean all && yum update kernel -y && yum -y reboot')
def verifying_dirty_cow():
	os.system('rpm -q --changelog kernel | grep CVE-2016-5195')
kernel()
verifying_dirty_cow()


            	



