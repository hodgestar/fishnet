""" Utilities for determining fishnet configuration. """

import execnet
import yaml


class FishnetConfig(object):
    """ Fishnet configuration. """
    def __init__(self):
        with open("./fishnet.yaml") as config_file:
            self._config = yaml.safe_load(config_file)

    @property
    def hosts(self):
        """ List of hosts. """
        return self._config['hosts']

    def execnet_group(self):
        """ Return an execnet group for hosts. """
        return execnet.Group(['ssh=%s' % host for host in self.hosts])


config = FishnetConfig()
