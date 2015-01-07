""" Utility for listing files. """

from fishnet.cmds.base import UnixCommand
from fishnet.config import config


def ls_local_op(channel, shell_glob):
    """ Perform an ls on the local machine. """
    import glob
    import subprocess

    filenames = list(glob.glob(shell_glob))
    p = subprocess.Popen(
        ["/bin/ls"] + filenames,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    for line in stdout.splitlines():
        channel.send("%s" % (line,))
    for line in stderr.splitlines():
        channel.send("[ERR] %s" % (line,))


class Ls(UnixCommand):
    """ List files. """

    args = ('shell_glob',)
    local_op = staticmethod(ls_local_op)


Ls.try_main(__name__, config.execnet_group)
