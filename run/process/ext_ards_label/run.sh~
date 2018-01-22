#!/usr/bin/env bash
# cmd_extractor  process/ext_ards_label
# {"cmd":"\n\n\t# TODO use temporary table\n\tdeepdive create table \"ards_label\"\n\tdeepdive sql 'INSERT INTO ards_label SELECT R0.p1_id AS \"ards_candidate.R0.p1_id\", R0.p2_id AS \"ards_candidate.R0.p2_id\", 0 AS column_2, NULL AS column_3\nFROM ards_candidate R0\n        \nUNION ALL\nSELECT R0.p1_id AS \"ards_candidate.R0.p1_id\", R0.p2_id AS \"ards_candidate.R0.p2_id\", 3 AS column_2, '\\''from_dbdata'\\'' AS column_3\nFROM ards_candidate R0, ards_dbdata R1\n        WHERE (lower(R1.med_name) = lower(R0.p1_name) AND lower(R1.ard_name) = lower(R0.p2_name))'\n\t# TODO rename temporary table to replace output_relation\n\t\n        ","dependencies":["ext_ards_candidate_by_map_ards_candidate"],"input_relations":["ards_candidate","ards_dbdata"],"output_relation":"ards_label","style":"cmd_extractor","dependencies_":["process/ext_ards_candidate_by_map_ards_candidate"],"input_":["data/ards_candidate","data/ards_dbdata"],"output_":"data/ards_label","name":"process/ext_ards_label"}
set -xeuo pipefail
cd "$(dirname "$0")"



export DEEPDIVE_CURRENT_PROCESS_NAME='process/ext_ards_label'


	# TODO use temporary table
	deepdive create table "ards_label"
	deepdive sql 'INSERT INTO ards_label SELECT R0.p1_id AS "ards_candidate.R0.p1_id", R0.p2_id AS "ards_candidate.R0.p2_id", 0 AS column_2, NULL AS column_3
FROM ards_candidate R0
        
UNION ALL
SELECT R0.p1_id AS "ards_candidate.R0.p1_id", R0.p2_id AS "ards_candidate.R0.p2_id", 3 AS column_2, '\''from_dbdata'\'' AS column_3
FROM ards_candidate R0, ards_dbdata R1
        WHERE (lower(R1.med_name) = lower(R0.p1_name) AND lower(R1.ard_name) = lower(R0.p2_name))'
	# TODO rename temporary table to replace output_relation
	
        



