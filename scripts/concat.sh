#!/usr/bin/env bash

path_fasta=${1}
path_annot=${2}

cat $path_fasta/*.fasta > all_fasta.fasta

cat $path_annot/*.tsv > all_annot.tsv
