#!/usr/bin/env python3
# coding=utf-8
import configparser
import argparse
import json
from libs.OpenStackAPI import OpenstackAuth, OpenstackImage, OpenstackFlavor, OpenstackServer


def get_image_id(auth_header, url, image_name):
    image_api = OpenstackImage(auth_header, url)
    image_list = image_api.get_images()
    image_id = image_api.get_image_detail(image_name, image_list)
    return image_id


def get_flavor_id(auth_header, url, image_id, flavor_name):
    flavor_api = OpenstackFlavor(auth_header, url)
    flavor_list = flavor_api.get_flavors(image_id)
    flavor_id = flavor_api.get_flavor_detail(flavor_name, flavor_list)
    return flavor_id


def main():
    "Using argparse to get instance name"
    parser = argparse.ArgumentParser(description='openstack-api')
    parser.add_argument('-s', '--servername', type=str,
                        help='Server Name(instance name)', required=True)
    openstackapi = parser.parse_args()

    # Init configuration
    config = configparser.ConfigParser()
    config.read('hostinfo.cfg')

    # Get token
    auth_header = OpenstackAuth.get_auth_token(
        config['OPENSTACK_API']['URL'],
        config['OPENSTACK_API']['USER'],
        config['OPENSTACK_API']['PASSWORD'])

    # Get Image of cirros
    image_id = get_image_id(
        auth_header,
        config['OPENSTACK_API']['URL'],
        config['IMAGE']['NAME'])

    # Get Flavor ID of m1.nano
    flavor_id = get_flavor_id(
        auth_header,
        config['OPENSTACK_API']['URL'],
        image_id,
        config['FLAVOR']['NAME'])

    # Create Server(instance)
    server_api = OpenstackServer(auth_header, config['OPENSTACK_API']['URL'])

    # Show Instance information
    server_list = server_api.get_servers()
    server_info = server_api.get_server_detail(
        openstackapi.servername, server_list)
    print(
        "\n\nThe instance named " +
        server_info['server']['name'] +
        " you created is success.")
    print("The IPv" +
          str(server_info['server']['addresses']['public'][0]['version']) +
          " of this instance is: " +
          server_info['server']['addresses']['public'][0]['addr'])
    try:
        print("The IPv" +
              str(server_info['server']['addresses']['public'][1]['version']) +
              " of this instance is: " +
              server_info['server']['addresses']['public'][1]['addr'])
    except BaseException:
        pass
    print("The whole info of this instance is as the followings: ")
    print(json.dumps(server_info, indent=2))


if __name__ == '__main__':
    main()
