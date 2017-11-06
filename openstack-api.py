#!/usr/bin/env python3
# coding=utf-8
import requests
import configparser


def get_auth_token(url, user, passwd):
    payload = {"auth": {"identity": {"methods": ["password"], "password": {
        "user": {"name": user, "domain": {"name": "default"}, "password": passwd}}}}}
    api_url = url + '/identity/v3/auth/tokens'
    result = requests.post(api_url, json=payload)
    print(result.json())
    return result.json()


def main():
    # Init configuration
    config = configparser.ConfigParser()
    config.read('hostinfo.cfg')

    auth_token = get_auth_token(
        config['OPENSTACK_API']['URL'],
        config['OPENSTACK_API']['USER'],
        config['OPENSTACK_API']['PASSWORD'])


if __name__ == '__main__':
    main()
