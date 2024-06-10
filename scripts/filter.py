#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 23:24:40 2024

@author: jrousseau
"""

import pandas as pd
import sys

path_dataframe = sys.argv[1]
identity = float(sys.argv[2])
overlap = float(sys.argv[3])
evalue = float(sys.argv[4])
path_output = sys.argv[5]

#path_dataframe = "diamond_alignment.tsv"
#identity = 80
#overlap = 80
#evalue = 1e-05

list_columns = [
    "qseqid", "sseqid", "pident", "ppos", "length", "mismatch",
    "gapopen", "qstart", "qend", "sstart", "send", "evalue", "bitscore"
    ]

df_alignment = pd.read_csv(path_dataframe, names = list_columns, sep = "\t")

index = df_alignment[(df_alignment["qseqid"] == \
                                 df_alignment["sseqid"])].index


df_alignment.drop(index, inplace = True)
    

df_alignment_filter = df_alignment[(df_alignment.pident >= identity) \
             & (df_alignment.ppos >= overlap) \
                 & (df_alignment.evalue <= evalue)]
             

df_alignment_filter.to_csv(f"{path_output}diamond_ssn_{identity}_{overlap}_{evalue}.tsv",
                           sep = "\t", index = False, header = False) 
