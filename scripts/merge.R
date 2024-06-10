#!/usr/bin/env Rscript

args <- commandArgs(TRUE)

annotation <- read.table(as.character(args[1]), sep = "\t", header = FALSE)
sequence_list <- read.table(as.character(args[2]), sep = "\t", header = FALSE)

df_merge <- merge(sequence_list, annotation, by = "V1", all.x = TRUE)

write.table(df_merge, file = paste(as.character(args[4]), as.character(args[3]), 
                                   "_vertices.attributes", sep = ""), 
            sep = "\t", row.names = FALSE, col.names = FALSE)