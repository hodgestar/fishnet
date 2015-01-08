""" Utility for cating files. """

from fishnet.cmds.base import UnixCommand
from fishnet.config import config


def cat_local_op(channel, shell_glob):
    """ Perform a cat on the local machine. """
    import glob
    import subprocess

    filenames = list(glob.glob(shell_glob))
    p = subprocess.Popen(
        ["/bin/cat"] + filenames,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    for line in stdout.splitlines():
        channel.send("%s" % (line,))
    for line in stderr.splitlines():
        channel.send("[ERR] %s" % (line,))


class Cat(UnixCommand):
    """ Cat files. """

    args = ('shell_glob',)
    local_op = staticmethod(cat_local_op)


Cat.try_main(__name__, config.execnet_group)
