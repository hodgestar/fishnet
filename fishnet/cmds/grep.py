""" Utility for grepping files and returning results. """

from fishnet.cmds.base import UnixCommand
from fishnet.config import config


def grep_local_op(channel, regex_pattern, shell_glob):
    """ Perform a grep on the local machine. """
    import glob
    import subprocess

    for filename in glob.glob(shell_glob):
        p = subprocess.Popen(
            ["/bin/grep", regex_pattern, filename],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        for line in stdout.splitlines():
            channel.send("[%s] %s" % (filename, line))
        for line in stderr.splitlines():
            channel.send("[ERR - %s] %s" % (filename, line))


class Grep(UnixCommand):
    """ Grep files matching a shell glob for lines matching a pattern. """

    args = ('regex_pattern', 'shell_glob')
    local_op = staticmethod(grep_local_op)


Grep.try_main(__name__, config.execnet_group)
