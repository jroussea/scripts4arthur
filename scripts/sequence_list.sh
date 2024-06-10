#!/usr/bin/env bash

proteome=${1}
output=${2}

# récupérer le nom des séquences fasta
awk 'sub(/^>/, "")' < $proteome > fasta_header

# récupéré la première partie des séquences (partie présente dans les résultats de diamond)
cut -d " " -f 1 fasta_header > $output

rm -f fasta_header
