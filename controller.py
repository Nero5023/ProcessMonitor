########################################################################
import psutil
import wx

from model import Process
from threading import Thread
from wx.lib.pubsub import setupkwargs
from wx.lib.pubsub import pub as Publisher
########################################################################
class ProcThread(Thread):
    """
    Gets all the process information we need as psutil isn't very fast
    """

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        Thread.__init__(self)
        self.start() 
        
    #----------------------------------------------------------------------
    def run(self):
        """"""
        processes = list(psutil.process_iter())
        procs = []
        cpu_percent = 0
        mem_percent = 0
        for p in processes:
            try:
                cpu = p.cpu_percent()
                mem = p.memory_percent()
                new_proc = Process(p.name,
                                   str(p.pid),
                                   p.exe,
                                   p.username,
                                   str(cpu),
                                   str(mem)
                                   )
                new_proc = Process(p.name(),
                                   str(p.pid),
                                   p.exe(),
                                   p.username(),
                                   str(cpu),
                                   str(mem)
                                   )
                procs.append(new_proc)
                cpu_percent += cpu
                mem_percent += mem
            except:
                print 'error'
                
        # send pids to GUI
        wx.CallAfter(Publisher.sendMessage, "update", msg = procs)
        
        number_of_procs = len(procs)
        wx.CallAfter(Publisher.sendMessage, "update_status", msg = (number_of_procs, cpu_percent, mem_percent))
        
            