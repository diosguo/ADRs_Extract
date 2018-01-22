#!/usr/bin/env bash
# cmd_extractor  process/ext_has_effect
# {"cmd":"\n\n\t# TODO use temporary table\n\tdeepdive create table \"has_effect\"\n\tdeepdive sql 'INSERT INTO has_effect SELECT DISTINCT R0.column_0, R0.column_1, 0 AS id, \nCASE WHEN R0.column_2 > 0 THEN true\n     WHEN R0.column_2 < 0 THEN false\n     ELSE NULL\nEND AS label\n          FROM ards_label_resolved R0\n        \n          '\n\t# TODO rename temporary table to replace output_relation\n\t\n        ","dependencies":["ext_ards_label_resolved"],"input_relations":["ards_label_resolved"],"output_relation":"has_effect","style":"cmd_extractor","dependencies_":["process/ext_ards_label_resolved"],"input_":["data/ards_label_resolved"],"output_":"data/has_effect","name":"process/ext_has_effect"}
set -xeuo pipefail
cd "$(dirname "$0")"



export DEEPDIVE_CURRENT_PROCESS_NAME='process/ext_has_effect'


	# TODO use temporary table
	deepdive create table "has_effect"
	deepdive sql 'INSERT INTO has_effect SELECT DISTINCT R0.column_0, R0.column_1, 0 AS id, 
CASE WHEN R0.column_2 > 0 THEN true
     WHEN R0.column_2 < 0 THEN false
     ELSE NULL
END AS label
          FROM ards_label_resolved R0
        
          '
	# TODO rename temporary table to replace output_relation
	
        



