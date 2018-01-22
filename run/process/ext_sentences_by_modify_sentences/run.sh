#!/usr/bin/env bash
# tsv_extractor  process/ext_sentences_by_modify_sentences
# {"dependencies":["ext_sentence_by_nlp_markup"],"input":" SELECT R0.doc_id AS \"sentence.R0.doc_id\", R0.sentence_index AS \"sentence.R0.sentence_index\", R0.sentence_text AS \"sentence.R0.sentence_text\", R0.tokens AS \"sentence.R0.tokens\", R0.lemmas AS \"sentence.R0.lemmas\", R0.pos_tags AS \"sentence.R0.pos_tags\", R0.ner_tags AS \"sentence.R0.ner_tags\", R0.doc_offsets AS \"sentence.R0.doc_offsets\", R0.dep_types AS \"sentence.R0.dep_types\", R0.dep_tokens AS \"sentence.R0.dep_tokens\"\nFROM sentence R0\n        \n          ","input_batch_size":"100000","input_relations":["sentence"],"output_relation":"sentences","parallelism":"1","style":"tsv_extractor","udf":"\"$DEEPDIVE_APP\"/udf/reco_med_ard_guo.py","dependencies_":["process/ext_sentence_by_nlp_markup"],"input_":["data/sentence"],"output_":"data/sentences","name":"process/ext_sentences_by_modify_sentences"}
set -xeuo pipefail
cd "$(dirname "$0")"



export DEEPDIVE_CURRENT_PROCESS_NAME='process/ext_sentences_by_modify_sentences'
export DEEPDIVE_LOAD_FORMAT=tsv

deepdive compute execute \
    input_sql=' SELECT R0.doc_id AS "sentence.R0.doc_id", R0.sentence_index AS "sentence.R0.sentence_index", R0.sentence_text AS "sentence.R0.sentence_text", R0.tokens AS "sentence.R0.tokens", R0.lemmas AS "sentence.R0.lemmas", R0.pos_tags AS "sentence.R0.pos_tags", R0.ner_tags AS "sentence.R0.ner_tags", R0.doc_offsets AS "sentence.R0.doc_offsets", R0.dep_types AS "sentence.R0.dep_types", R0.dep_tokens AS "sentence.R0.dep_tokens"
FROM sentence R0
        
          ' \
    command='"$DEEPDIVE_APP"/udf/reco_med_ard_guo.py' \
    output_relation='sentences' \
    #



