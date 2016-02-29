__author__ = 'donal'
__project__ = 'tinyFeet'

import os
import bmemcached

def build_mc_config():
    SERVERS = os.environ.get('MEMCACHIER_SERVERS', '').split(',')
    MC_USER = os.environ.get('MEMCACHIER_USERNAME', '')
    MC_PWD = os.environ.get('MEMCACHIER_PASSWORD', '')
    return bmemcached.Client(SERVERS, MC_USER, MC_PWD)