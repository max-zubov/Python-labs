#!/usr/bin/env python

import json
import psutil
import datetime
from collections import namedtuple
import time

def nmtpl_dict(nmtpl):
    """Converting named tupl to dict."""
    
    keylist=nmtpl._fields
    vallist=tuple(nmtpl)
    return({keylist[i]: vallist[i] for i in range(len(keylist))})

def monitor():
    """request system parameters and return them as a named tuple."""
    
    info = namedtuple( "info", "date_time cpu_count cpu_logical_count load_average cpu_percent cpu_times \
    swap_memory virtual_memory disk_partitions disk_io_counters net_io_counters" )
    
    return( info( date_time = datetime.datetime.now(),
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
    

def jsonLog( file_name, m, n):
    """Write monitoring data to logfile in json format."""
    
    json_snapshot={'SNAPSHOT-'+ str(n): str(m.date_time),
    'OverallSystemData': { 'CPU_count': [str(m.cpu_count), str(m.cpu_logical_count)]}, 
    'OverallCPUload': {'LoadOverage': m.load_average, 'Percent': m.cpu_percent, \
    m.cpu_times.__class__.__name__: nmtpl_dict(m.cpu_times) },
    'OverallMemoryUsage': { m.swap_memory.__class__.__name__: nmtpl_dict(m.swap_memory)},
    'OverallVirtualMemoryUsage': {m.virtual_memory.__class__.__name__: nmtpl_dict(m.virtual_memory)},
    'IOinformation': {'DiskPartitions': [ nmtpl_dict(partition) for partition in m.disk_partitions ], \
    m.disk_io_counters.__class__.__name__: nmtpl_dict(m.disk_io_counters)},
    'NetworkInformation': { m.net_io_counters.__class__.__name__: nmtpl_dict(m.net_io_counters)}}
    
    #print(json_snapshot)
    #print(json.dumps(json_snapshot, indent=4, sort_keys=False))
    
    with open(file_name, "a+") as log_file:
        content = log_file.read()
        de = json.JSONDecoder().decode(content) if content else []
        de.append(json_snapshot)
        en = json.JSONEncoder().encode(de)
        log_file.write(en)

        
def txtLog(file_name, m, n):
    """Write monitoring data to logfile in txt format."""

    txt_snapshot="""SNAPSHOT-{}: {}\n CPU_Count {}/{}\n CPU_Load_Average {}\n CPU_Percent {}\n CPU_Times {}\n \
Memory {}/{}\n Swap {}/{}\n Disk_Partitions {}\n Disk_IO {}/{}\n Network_IO {}/{}\n\n""" \
    .format(n, str(m.date_time), m.cpu_count, m.cpu_logical_count, m.load_average, m.cpu_percent, m.cpu_times.user, \
    m.virtual_memory.total, m.virtual_memory.used, m.swap_memory.total, m.swap_memory.used, \
    ["{} -> {}".format(p.device, p.mountpoint) for p in m.disk_partitions ], \
    m.disk_io_counters.read_count, m.disk_io_counters.write_count, \
    m.net_io_counters.bytes_sent, m.net_io_counters.bytes_recv )
        
    #print(txt_snapshot)
    with open(file_name, "a+") as log_file:
        log_file.write(txt_snapshot)   

    
def main():

    #Reading parameters from json config file. 
    with open("monitor.conf", "r") as conf_file:
        conf = json.load(conf_file)

    #Create new logfile.
    if conf['output'] == 'json':    new_file = 'log_file.json'
    else:    new_file = 'log_file.txt'
    f=open(new_file, "w") 
    f.close()
    i=0
       
    while True:
        i=i+1
        if conf['output'] == 'json':
            jsonLog('log_file.json', monitor(), i)
        else:
            txtLog('log_file.txt', monitor(), i)
        time.sleep(int(conf['interval']))    
main()
    