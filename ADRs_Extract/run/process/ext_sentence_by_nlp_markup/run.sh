#!/usr/bin/env bash
# tsv_extractor  process/ext_sentence_by_nlp_markup
# {"input":" SELECT R0.id AS \"articles.R0.id\", R0.content AS \"articles.R0.content\"\nFROM articles R0\n        \n          ","input_batch_size":"100000","input_relations":["articles"],"output_relation":"sentence","parallelism":"1","style":"tsv_extractor","udf":"\"$DEEPDIVE_APP\"/udf/fenci.py","dependencies_":[],"input_":["data/articles"],"output_":"data/sentence","name":"process/ext_sentence_by_nlp_markup"}
set -xeuo pipefail
cd "$(dirname "$0")"



export DEEPDIVE_CURRENT_PROCESS_NAME='process/ext_sentence_by_nlp_markup'
export DEEPDIVE_LOAD_FORMAT=tsv

deepdive compute execute \
    input_sql=' SELECT R0.id AS "articles.R0.id", R0.content AS "articles.R0.content"
FROM articles R0
        
          ' \
    command='"$DEEPDIVE_APP"/udf/fenci.py' \
    output_relation='sentence' \
    #



