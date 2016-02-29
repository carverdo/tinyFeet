__author__ = 'donal'
__project__ = 'tinyFeet'

import os
import bmemcached
"""

servers = os.environ.get('MEMCACHIER_SERVERS', '').split(',')
user = os.environ.get('MEMCACHIER_USERNAME', '')
pass = os.environ.get('MEMCACHIER_PASSWORD', '')
"""


"""
MEMCACHIER_SERVERS
mc4.dev.eu.ec2.memcachier.com:11211

MEMCACHIER_USERNAME
f60f00

MEMCACHIER_PASSWORD
6630644b76843f290efe2ec3fc93a551
"""

servers = ['mc4.dev.eu.ec2.memcachier.com:11211']
user = 'f60f00'
pwd = '6630644b76843f290efe2ec3fc93a551'

mc =  bmemcached.Client(servers, user, pwd)
mc.set('key', 'value')
print mc.get('key')
