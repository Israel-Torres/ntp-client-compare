#!/usr/bin/python
__author__ = 'israeltorres'
# NTP Time Compare
import ntplib
from time import ctime
c = ntplib.NTPClient()

response = c.request('pool.ntp.org')
poolntporg = ctime(response.tx_time)

response = c.request('time.apple.com')
appletime = ctime(response.tx_time)

response = c.request('time.windows.com')
mstime000 = ctime(response.tx_time)

response = c.request('10.160.10.8')
ntp010008 = ctime(response.tx_time)

print ("%s : pool.ntp.org" % poolntporg)
print ("%s : time.apple.com" % appletime)
print ("%s : time.windows.com" % mstime000)
print ("%s : 10.160.10.8" % ntp010008)
