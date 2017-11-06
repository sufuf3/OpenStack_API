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
        print("Header: ")
        print(header)
        print("All result: ")
        print(result.json())
        return token


class OpenstackImage():
    def create_image():
        pass

    def detail_image():
        pass

    def image_list():
        pass


class OpenstackFlavor():
    def create_flavor():
        pass

    def detail_flavor():
        pass

    def flavor_list():
        pass
