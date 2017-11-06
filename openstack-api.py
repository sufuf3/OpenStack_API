#!/usr/bin/env python3
# coding=utf-8
import requests
import configparser
from libs.OpenStackAPI import OpenstackAuth


def main():
    # Init configuration
    config = configparser.ConfigParser()
    config.read('hostinfo.cfg')

    # Get token
    auth_token = OpenstackAuth.get_auth_token(
        config['OPENSTACK_API']['URL'],
        config['OPENSTACK_API']['USER'],
        config['OPENSTACK_API']['PASSWORD'])


if __name__ == '__main__':
    main()
