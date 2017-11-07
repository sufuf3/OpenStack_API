OpenStack API Homework 3-1
===

# Development Guide  
# Develop environment prepare  
OS: Ubuntu  

```bash
$ apt-get install python3-venv  
$ python3 -m venv venv  
$ source venv/bin/activate  
$ pip3 install -r requirements.txt  
$ autopep8 --in-place --aggressive --aggressive openstack-api.py
$ flake8 openstack-api.py
```
  
# Execute  

```bash
$ python openstack-api.py -s [instance_name]
```
  
Reference: https://hackmd.io/s/BJMZcFQ0b  
