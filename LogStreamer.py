#!/usr/bin/python3


from LogGenerator import *
import time

destData = time.strftime("/var/log/trainsdata/%Y%m%d-%H%M%S.log")
placeholder="LastLine.txt"

lg = LogGenerator(destData, "trips.txt", placeholder)
print(lg)

lg.GenerateLog(100)
