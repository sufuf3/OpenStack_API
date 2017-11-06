#!/usr/bin/env python3
# coding=utf-8
import configparser
from libs.OpenStackAPI import OpenstackAuth, OpenstackImage, OpenstackFlavor


def main():
    # Init configuration
    config = configparser.ConfigParser()
    config.read('hostinfo.cfg')

    # Get token
    auth_header = OpenstackAuth.get_auth_token(
        config['OPENSTACK_API']['URL'],
        config['OPENSTACK_API']['USER'],
        config['OPENSTACK_API']['PASSWORD'])

    # Get Image of cirros
    image_api = OpenstackImage(auth_header, config['OPENSTACK_API']['URL'])
    image_list = image_api.get_images()
    image_id = image_api.get_image_detail(config['IMAGE']['NAME'], image_list)

    # Get Flavor ID of m1.nano
    flavor_api = OpenstackFlavor(auth_header, config['OPENSTACK_API']['URL'])
    flavor_list = flavor_api.get_flavors(image_id)
    flavor_id = flavor_api.get_flavor_detail(
        config['FLAVOR']['NAME'], flavor_list)

    # Create Server(instance)

    # Show Instance information


if __name__ == '__main__':
    main()
