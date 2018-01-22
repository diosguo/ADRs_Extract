#!/usr/bin/env bash
# tsv_extractor  process/ext_ards_candidate_by_map_ards_candidate
# {"dependencies":["ext_medicine_mention_by_map_medicine_mention","ext_ards_mention_by_map_ards_mention"],"input":" SELECT R0.mention_id AS \"medicine_mention.R0.mention_id\", R0.mention_text AS \"medicine_mention.R0.mention_text\", R1.mention_id AS \"ards_mention.R1.mention_id\", R1.mention_text AS \"ards_mention.R1.mention_text\"\nFROM medicine_mention R0, ards_mention R1\n        WHERE R1.doc_id = R0.doc_id  AND R1.sentence_index = R0.sentence_index \n          ","input_batch_size":"100000","input_relations":["medicine_mention","ards_mention"],"output_relation":"ards_candidate","parallelism":"1","style":"tsv_extractor","udf":"\"$DEEPDIVE_APP\"/udf/map_ards_candidate.py","dependencies_":["process/ext_medicine_mention_by_map_medicine_mention","process/ext_ards_mention_by_map_ards_mention"],"input_":["data/medicine_mention","data/ards_mention"],"output_":"data/ards_candidate","name":"process/ext_ards_candidate_by_map_ards_candidate"}
set -xeuo pipefail
cd "$(dirname "$0")"



export DEEPDIVE_CURRENT_PROCESS_NAME='process/ext_ards_candidate_by_map_ards_candidate'
export DEEPDIVE_LOAD_FORMAT=tsv

deepdive compute execute \
    input_sql=' SELECT R0.mention_id AS "medicine_mention.R0.mention_id", R0.mention_text AS "medicine_mention.R0.mention_text", R1.mention_id AS "ards_mention.R1.mention_id", R1.mention_text AS "ards_mention.R1.mention_text"
FROM medicine_mention R0, ards_mention R1
        WHERE R1.doc_id = R0.doc_id  AND R1.sentence_index = R0.sentence_index 
          ' \
    command='"$DEEPDIVE_APP"/udf/map_ards_candidate.py' \
    output_relation='ards_candidate' \
    #



