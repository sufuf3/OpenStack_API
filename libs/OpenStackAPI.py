#!/usr/bin/env python3
# coding=utf-8
import requests


class OpenstackAuth():
    def get_auth_token(url, user, passwd):
        payload = {
            "auth": {
                "identity": {
                    "methods": ["password"],
                    "password": {
                        "user": {
                            "name": user,
                            "domain": {"name": "default"},
                            "password": passwd
                        }
                    }
                },
                'scope': {
                    'project': {
                        'name': 'admin',
                        'domain': {
                                'name': 'Default'
                        }
                    }
                }
            }}
        header = {'Content-type': 'application/json'}
        api_url = url + '/identity/v3/auth/tokens'
        result = requests.post(api_url, headers=header, json=payload)
        token = result.headers['X-Subject-Token']
        header = {'Content-type': 'application/json',
                  'X-Auth-Token': token}
        print("Get Token: " + token)
        return header


class OpenstackImage():
    def __init__(self, header, url):
        self.header = header
        self.url = url

    def get_images(self):
        api_url = self.url + '/image/v2/images'
        payload = {"X-Auth-Token": self.header["X-Auth-Token"]}
        result = requests.get(api_url, headers=payload)
        return result.json()['images']

    def get_image_detail(self, imagename, image_list):
        for i in image_list:
            if i['name'].startswith(imagename):
                print('Image ID is: ' + i['id'])
                return i['id']
        print('There is no image named: ' + imagename)


class OpenstackFlavor():
    def __init__(self, header, url):
        self.header = header
        self.url = url

    def get_flavors(self, image_id):
        api_url = self.url + '/compute/v2.1/flavors'
        payload = {"X-Auth-Token": self.header["X-Auth-Token"]}
        result = requests.get(api_url, headers=payload)
        return result.json()['flavors']

    def get_flavor_detail(self, flavor_name, flavor_list):
        for i in flavor_list:
            if i['name'].startswith(flavor_name):
                print('Flavor ID is: ' + i['id'])
                return i['id']
        print('There is no flavor named: ' + flavor_name)


class OpenstackServer():
    def __init__(self, header, url):
        self.header = header
        self.url = url

    def get_servers(self):
        api_url = self.url + '/compute/v2.1/servers'
        payload = {"X-Auth-Token": self.header["X-Auth-Token"]}
        result = requests.get(api_url, headers=payload)
        return result.json()['servers']

    def get_server_detail(self, server_name, server_list):
        for i in server_list:
            if i['name'] == server_name:
                api_url = self.url + '/compute/v2.1/servers/' + i['id']
                payload = {"X-Auth-Token": self.header["X-Auth-Token"]}
                result = requests.get(api_url, headers=payload)
                return result.json()
