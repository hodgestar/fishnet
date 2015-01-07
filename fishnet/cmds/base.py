""" Base classes for easily creating commands. """


def local_op_undefined(channel, **kw):
    """ Local operation not implemented. """
    raise NotImplementedError("Operation not implemented.")


class UnixCommand(object):
    """ Base class for traditional Unix command line utilities. """

    # tuple of names of positional arguments
    args = ()

    # local operation that args are passed to, has to be a pure function
    local_op = staticmethod(local_op_undefined)

    @classmethod
    def remote_op(cls, gw, args):
        """ Perform operation remotely via an execnet gateway. """
        kw = dict(zip(cls.args, args))
        channel = gw.remote_exec(cls.local_op, **kw)
        for line in channel:
            yield line

    @classmethod
    def remote_main(cls, sys_args, group):
        """ Run operation over gateways machines, reading arguments from the
            command line and writing results to stdout.
        """
        args = sys_args[1:]
        if len(args) != len(cls.args):
            raise ValueError("Usage: %s %s" % (
                sys_args[0], " ".join(cls.args)))
        for gw in group:
            for line in cls.remote_op(gw, args):
                print "[%s] %s" % (gw.remoteaddress, line)

    @classmethod
    def try_main(cls, module_name, group_func):
        if module_name == "__main__":
            import sys
            cls.remote_main(sys.argv, group_func())
