#!/usr/bin/python3

from LogGenerator import *
from sys import argv
import time
import random

# Folder to store the log files (requires using a GNU-Linux OS)
baseDestData = time.strftime("/var/log/trainsdata")

# Min and Max values for log generation
MIN_VALUE = 1   
MAX_VALUE = 120

# Interval (in seconds) between each log generation
SECONDS_BETWEEN_LOGS = 8

# Uncomment this few lines to test the script without command line arguments

# tableName = "trips"
# destData = f"{baseDestData}/{tableName}"  # It's important to separate different data logs
# placeholder=f"{tableName}_LastLine.txt"   # And also its files where they store current last line

def stream_logs(destData, sourceFile, curr_line_file):
    log_gen = LogGenerator(destData, sourceFile, curr_line_file)
    while(True):
        logs_to_generate = random.randrange(MIN_VALUE, MAX_VALUE)
        log_gen.GenerateLog(logs_to_generate)
        time.sleep(SECONDS_BETWEEN_LOGS)
        
    
if __name__ == '__main__':
    if len(argv) != 3:
        # Example1: sudo ./LogStreamer myTable mySourceFile.txt
        # Example2: sudo ./LogStreamer myTable mySourceFile.csv
        raise("Usage: sudo ./LogStreamer <tableName> <sourceFile>") 
    else:
        tableName = argv[1]
        sourceFile = argv[2]
        destData = f"{baseDestData}/{tableName}"  # It's important to separate different data logs
        curr_line_file = f"{tableName}_LastLine.txt" # And also its files where they store current last line
        stream_logs(destData, sourceFile, curr_line_file)