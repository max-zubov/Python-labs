#!/usr/bin/env python

import json
import psutil
import datetime
from collections import namedtuple
import time

info = namedtuple( "info", "date_time cpu_count cpu_logical_count load_average cpu_percent cpu_times \
swap_memory virtual_memory disk_partitions disk_io_counters net_io_counters" )

def nmtpl_dict(nmtpl):
    """Converting named tupl to dict."""
    keylist=nmtpl._fields
    vallist=tuple(nmtpl)
    return({keylist[i]: vallist[i] for i in range(len(keylist))})


class monitor:
    
    def getinfo(self):
        return(info( date_time = datetime.datetime.now(),
        cpu_count = psutil.cpu_count(),
        cpu_logical_count = psutil.cpu_count(logical=True),
        load_average = psutil.getloadavg(),
        cpu_percent = psutil.cpu_percent(),
        cpu_times = psutil.cpu_times(percpu=False),
        swap_memory = psutil.swap_memory(),
        virtual_memory = psutil.virtual_memory(),
        disk_partitions = psutil.disk_partitions(all=False),
        disk_io_counters = psutil.disk_io_counters(perdisk=False),
        net_io_counters = psutil.net_io_counters()) )
    

class logfile:
    def __init__(self, filename):
        self.logname=filename
        f=open(self.logname, 'w' )
        f.close()
        self.n=0
    def write(self, rec):
        with open(self.logname, "a+") as f:
            f.write(rec)   
            
class txtlog(logfile,monitor):
    def loggin(self):
        self.n=self.n+1
        m=self.getinfo()
        snapshot="""SNAPSHOT-{}: {}\n CPU_Count {}/{}\n CPU_Load_Average {}\n CPU_Percent {}\n CPU_Times {}\n \
Memory {}/{}\n Swap {}/{}\n Disk_Partitions {}\n Disk_IO {}/{}\n Network_IO {}/{}\n\n""" \
        .format(self.n, str(m.date_time), m.cpu_count, m.cpu_logical_count, m.load_average, m.cpu_percent, m.cpu_times.user, \
        m.virtual_memory.total, m.virtual_memory.used, m.swap_memory.total, m.swap_memory.used, \
        ["{} -> {}".format(p.device, p.mountpoint) for p in m.disk_partitions ], \
        m.disk_io_counters.read_count, m.disk_io_counters.write_count, \
        m.net_io_counters.bytes_sent, m.net_io_counters.bytes_recv )
        
        self.write(snapshot)

            
            
class jsonlog(logfile,monitor):
        
    def write(self, rec):
        with open(self.logname, "a+") as f:
            content = f.read()
            de = json.JSONDecoder().decode(content) if content else []
            de.append(rec)
            en = json.JSONEncoder().encode(de)
            f.write(en)
    
    def loggin(self):
        self.n=self.n+1
        m=self.getinfo()
        snapshot={'SNAPSHOT-'+ str(self.n): str(m.date_time),
        'OverallSystemData': { 'CPU_count': [str(m.cpu_count), str(m.cpu_logical_count)]}, 
        'OverallCPUload': {'LoadOverage': m.load_average, 'Percent': m.cpu_percent, \
        m.cpu_times.__class__.__name__: nmtpl_dict(m.cpu_times) },
        'OverallMemoryUsage': { m.swap_memory.__class__.__name__: nmtpl_dict(m.swap_memory)},
        'OverallVirtualMemoryUsage': {m.virtual_memory.__class__.__name__: nmtpl_dict(m.virtual_memory)},
        'IOinformation': {'DiskPartitions': [ nmtpl_dict(partition) for partition in m.disk_partitions ], \
        m.disk_io_counters.__class__.__name__: nmtpl_dict(m.disk_io_counters)},
        'NetworkInformation': { m.net_io_counters.__class__.__name__: nmtpl_dict(m.net_io_counters)}}
    
        self.write(snapshot)
        

def main():

    #Reading parameters from json config file. 
    with open("monitor.conf", "r") as conf_file:
        conf = json.load(conf_file)

    #Create new logfile.
    if conf['output'] == 'json':    log_file = jsonlog('log_file.json')
    else:    log_file = txtlog('log_file.txt') 
       
    while True:
        log_file.loggin()
        time.sleep(int(conf['interval']))
    
main()
    