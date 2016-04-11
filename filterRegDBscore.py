#!/usr/bin/env python

import sys


'''
Script will a a file that has been annotated by RegulomeDB and scored, and filter out 
unwanted scores.  Output file will only contain the positions with desired scores.

run program as:
filterRegDBscore.py <name of scored file to filter>
'''

def main():

    inFileName = sys.argv[1]

    WantedScores = ["1a","1b","1c","1d","1e","1f","2a","2b","2c","5"]

    with open (inFileName, 'r') as infile:  #when you use "with open" you don't have to close the file later
    	with open (inFileName + ".filteredScores", "w") as filteredscores: 
            for line in infile:
            	(chrom, pos, snpID, data, score)= line.strip("\n").split("\t")
            	if score in WantedScores:
            		filteredscores.write(line)

if __name__ == '__main__':
    main()
            	


    