#!/usr/bin/env bash

dataframe=${1}
annotation=${2}
parameters=${3}
output=${4}

cut -f 1 $dataframe > col1
cut -f 2 $dataframe > col2

cat col1 col2 > sequence_filter

./scripts/merge.R $annotation sequence_filter $parameters $output

rm -f col1 col2 sequence_filter
