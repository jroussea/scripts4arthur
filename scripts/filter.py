#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 15:02:43 2024

@author: jeremy
"""

import sys
import pandas as pd


def main(diamond_alignment, output, query, subject, identity, overlap, evalue, 
         identity_min, overlap_min, evalue_max):

    df_diamond_alignment = pd.read_table(diamond_alignment, header=None)
    df_diamond_alignment.columns = \
        [ i for i in range(1, len(df_diamond_alignment.columns)+1, 1) ]
    
    index = df_diamond_alignment[(df_diamond_alignment[query] == \
                                  df_diamond_alignment[subject])].index
    
    df_diamond_alignment.drop(index, inplace = True)
    
    
    
    df_diamond_alignment = df_diamond_alignment[(df_diamond_alignment[identity] >= identity_min) & \
                               (df_diamond_alignment[overlap] >= overlap_min) & \
                                   (df_diamond_alignment[evalue] <= evalue_max)]
        
    df_diamond_alignment = df_diamond_alignment[[query,subject,identity,overlap,evalue]]
    
    df_diamond_alignment.rename(columns = {1:"query", 2:"subject", 3:"identity", 4:"overlap", 12:"evalue"}, inplace = True)
    
    df_diamond_alignment.to_csv(f"{output}/diamond_ssn_{identity_min}_{overlap_min}_{evalue_max}.tsv",
                                sep = "\t", index = False, header = True) 


if __name__ == '__main__':
   
    diamond_alignment = sys.argv[1]
    output = sys.argv[2]
    
    query = int(sys.argv[3])
    subject = int(sys.argv[4])
    identity = int(sys.argv[5])
    overlap = int(sys.argv[6])
    evalue =  int(sys.argv[7])
    
    identity_min = float(sys.argv[8])
    overlap_min = float(sys.argv[9])
    evalue_max = float(sys.argv[10])
    
    main(diamond_alignment, output, query, subject, identity, overlap, evalue, 
         identity_min, overlap_min, evalue_max)




#diamond_alignment = "diamond_alignment"
#query = 1
#subject = 2
#identity = 3 
#overlap = 4
#evalue =  12

#identity_min = 80
#overlap_min = 80
#evalue_max = 1e-5

