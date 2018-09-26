import sys
import os
import logging
import pprint

# do we get a useful __name__ here?
log = logging.getLogger(__name__)

log_format = '[%(asctime)s %(process)05d %(levelname)-0.1s] %(name)s %(funcName)s:%(lineno)d - %(message)s'
log_filename = '/tmp/ansible_testing_content_mean_init.log'

foo = os.path.expanduser('~/.ssh/id_rsa.pub')

logging.basicConfig(level=logging.DEBUG,
                    filename=log_filename,
                    format=log_format)

log.debug('ran mean init')

with open(foo, 'r') as fd:
    pub = fd.read()
    log.debug('pub pub pub: %s', pub)

log.debug('sys.path: %s', pprint.pformat(sys.path))
