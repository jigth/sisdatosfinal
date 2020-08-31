#!/usr/bin/python3

# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 12:01:21 2019

@author: Frank

Modified on Sat Aug 30 2020
@dochoam

"""

import csv
import time
import sys  

# sourceData = "OnlineRetail.csv"
# placeholder = "LastLine.txt"
# destData = time.strftime("/var/log/trainsdata/%Y%m%d-%H%M%S.log")

class LogGenerator():
    def __init__(self, destData, sourceData, placeholder):
            self.destData = destData
            self.sourceData = sourceData
            self.placeholder = placeholder

    def __str__(self):
        return f"destData= {self.destData}\nsourceData= {self.sourceData}\nplaceHolder= {self.placeholder}"

    def GetLineCount(self):
        with open(self.sourceData) as f:
            for i, l in enumerate(f):
                pass
        return i

    def MakeLog(self, startLine, numLines):    
        with open(self.sourceData, 'r') as csvfile:
            with open(self.destData, 'w') as dstfile:
                reader = csv.reader(csvfile)
                writer = csv.writer(dstfile)
                next (reader) #skip header
                inputRow = 0
                linesWritten = 0
                for row in reader:
                    inputRow += 1
                    if (inputRow > startLine):
                        writer.writerow(row)
                        linesWritten += 1
                        if (linesWritten >= numLines):
                            break
                return linesWritten
            
    # Generate a log by reading and copying N lines from a file (source) to another file (destination)
    def GenerateLog(self, numLines):  # TODO: MODIFY CODE TO ONLY HAVE 'numLines' DEFINED HERE IN THE FUNCTION ARGUMENTS
        #numLines = 100
        #if (len(sys.argv) > 1):  # ARGV !!!!!!!!!!!!!!!!!!!!!!!!!!
        #    numLines = int(sys.argv[1])
        startLine = 0            
        try:
            with open(self.placeholder, 'r') as f:
                for line in f:
                    startLine = int(line)
        except IOError:
            startLine = 0

        print("Writing " + str(numLines) + " lines starting at line " + str(startLine) + "\n")

        totalLinesWritten = 0
        linesInFile = self.GetLineCount()

        while (totalLinesWritten < numLines):
            linesWritten = self.MakeLog(startLine, numLines - totalLinesWritten)
            totalLinesWritten += linesWritten
            startLine += linesWritten
            if (startLine >= linesInFile): # Restart start line when the whole file has been read
                startLine = 0
                
        print("Wrote " + str(totalLinesWritten) + " lines.\n")
            
        with open(self.placeholder, 'w') as f: # Write the new "startLine" in file (lastLine.txt)
            f.write(str(startLine))
