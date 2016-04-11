#!/usr/bin/env python

import sys


'''
Script will convert a filtered-score file to BED format.
Output file will show chrom, start, and end, for the scored variants of interest.
This will be used to apply a closest-gene script comparing this BED file and a reference BED file.

run program as:
filtered2bed.py <name of score-filtered file to convert to BED format>
'''

def main():

    inFileName = sys.argv[1]

    with open (inFileName, 'r') as infile:
    	with open (inFileName + ".bed", "w") as filteredBed: 
            for line in infile:
            	(chrom, pos, snpID, data, score)= line.strip("\n").split("\t")
            	filteredBed.write(chrom + "\t" + str(int(pos)-1) + "\t" + pos+ "\n") 
           		#BED format is zero-based; VCF is 1-based
           		#So, BED start coordinate is one less than VCF start.
           		#BED ending coordinate is non-inclusive, so pos-1 to pos refers to a single base

if __name__ == '__main__':
    main()
            	