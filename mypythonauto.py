#!/usr/bin/python
import os
def install_apache():
       print("installing apache server")
       os.system('sudo yum -y install httpd')
       print("enabling apache server")
       os.system('sudo systemctl enable httpd.service')
       print("starting apache server")
       os.system('sudo systemctl start httpd.service')
       print('please you open the security settings for port 80 on your server, you should see the apache start page')
install_apache()
def hello_world():
	print('Hello NTI-300!')
	print('This is Fadil python automation script')	      
hello-world()
def setup_install():
    print('installing pip and virtualenv so we can give django its own version of python')
    os.system('rpm -iUvh https://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-8.noarch.rpm')
    os.system('yum -y install python-pip && pip install --upgrade pip')
    os.system('pip install virtualenv')
    os.chdir('/opt')
    os.mkdir('/opt/django')
    os.chdir('/opt/django')
    os.system('virtualenv django-env')
    os.system('chown -R ec2-user /opt/django')   
setup_install()
def django_install():
    print('activating virtualenv and installing django after pre-requirements have been met')
                                                 
    os.system('source /opt/django/django-env/bin/activate && pip install django')
                                                 
    os.chdir('/opt/django')
    os.system('source /opt/django/django-env/bin/activate ' + \
              '&& django-admin --version ' + \
              '&& django-admin startproject project1')
django_install()
def django_start():
    print('starting django')
    os.system('source /opt/django/django-env/bin/activate && python /opt/django/project1/manage.py runserver 0.0.0.0:8000&')
django_start()

# installing git
import os
def install_git():
	print('installing git')
	os.system('yum -y install git')
	os.system('git clone https://github.com/fjemal/NTI-300-repository')
install_git()
import os
def install package():
	print('installing package')
	os.system('yum -y install '+package)
intstallpackage()

def install_tree():
      os.systemc('yum -y install tree')
install_tree()

def mailx():
	print('installing mailx')
	os.system('yum -y install mailx')
mailx()
def kernel():
	print('installing kernel')
	os.system('yum -y clean all && yum update kernel -y && yum -y reboot')
kernel()
	def verifying_dirty_cow():
	os.system('rpm -q --changelog kernel | grep CVE-2016-5195')

verifying_dirty_cow()


            	



