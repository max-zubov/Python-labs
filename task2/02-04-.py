#!/usr/bin/python

# script for find the ten often ip addresses in a logfile

logFile = open("access.log", "r").readlines()
ipCount = {}

for line in logFile:
    ipAddr = line.split(" ")[0]
    if ipAddr not in ipCount:    ipCount[ipAddr] = 0
    ipCount[ipAddr] += 1

for ip in dict(sorted(ipCount.items(), key=lambda i:i[1], reverse=True)[:10]):
    print("{0:15} : {1}".format(ip, ipCount[ip]))
