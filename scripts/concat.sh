#!/usr/bin/env bash

path_fasta=${1}
path_annot=${2}
output_fasta=${3}
output_tsv=${4}

cat $path_fasta > $output_fasta

cat $path_annot > $output_tsv


cat $path_fasta

cat $path_annot
