#!/usr/bin/env bash

protein=${1}
colA=${2}
colB=${3}
database=${4}

cut -f $protein,$colA,$colB all_annotation.tsv | grep $database > file_select.tsv



