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
	os.system('yum -y rpm -q --changelog kernel | grep CVE-2016-5195')
kernel()
verifying_dirty_cow()
import os
def users():
	print('creating crontab User Alert')
        os.system('users=$(/usr/bin/who | grep -c"")')
def users():
	print('creating crontab User Alert')
        os.system('users=$(/usr/bin/who | grep -c"")')
        os.system('if["$users">=1]; echo there is morethan one user logged in')
	os.system('else: echo lessthan one user logged in')
	os.system('chmod +x /home/ec2-user/test2.sh')
        os.system('crontab -l; echo * * * * * /home/ec2-user/test2.sh | mail -s\"User Alert\" fadliebra2012@gmail.com')
	
users()
            	



