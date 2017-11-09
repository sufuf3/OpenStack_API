OpenStack API Homework 3-1
===

## Description

This howework is based on https://hackmd.io/s/BJMZcFQ0b.

The required tasks we are trying to complete (and succeed at last) are

1. Create an instance whatever it is called based on `cirros`  image and `m1.nano` flavor.
2. Print the IP of the above instance on the screen.

##Environment Requirement

Prepare a Ubuntu like OS and run the following commands:

```bash
$ apt-get install python3-venv  
$ python3 -m venv venv  
$ source venv/bin/activate  
$ pip3 install -r requirements.txt  
$ autopep8 --in-place --aggressive --aggressive openstack-api.py
$ flake8 openstack-api.py
```

Please let us know if you meet any problem here.

## Execute

```bash
$ python openstack-api.py -s [instance_name]
```

This will first show auth token, image ID, flavor ID on the screen.
Next, it builds instance using token, image ID, flavor ID just shown. 
Finally, the details including IPv4, IPv6 addresses can be seen on the screen.

## Others

Please note that you **can** create an instance even there has been another instance having a same name.