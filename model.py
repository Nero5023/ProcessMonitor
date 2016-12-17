########################################################################
class Process(object):
    """
    Definition of Process model for ObjectListView
    """

    #----------------------------------------------------------------------
    def __init__(self, name, pid, exe, user, cpu, mem, rss, vms, pfaults, pageins):
        """Constructor"""
        self.name = name
        self.pid = pid
        self.exe = exe
        self.user = user
        self.cpu = cpu
        self.mem = mem
        self.rss = rss
        self.vms = vms
        self.pfaults = pfaults
        self.pageins = pageins