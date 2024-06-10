#!/usr/bin/env bash

fasta=${1}
db=${2}
alignment=${3}

diamond makedb --in $fasta --db $db

diamond blastp -d $db \
	       -q $fasta \
	       -o $alignment \
	       -e 1e-5 \
	       --sensitive \
	       --outfmt 6 qseqid sseqid pident ppos length mismatch gapopen qstart qend sstart send evalue bitscore
