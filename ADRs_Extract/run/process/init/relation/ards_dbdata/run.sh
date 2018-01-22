#!/usr/bin/env bash
# cmd_extractor  process/init/relation/ards_dbdata
# {"style":"cmd_extractor","cmd":"deepdive create table 'ards_dbdata' && deepdive load 'ards_dbdata'","dependencies_":["process/init/app"],"output_relation":"ards_dbdata","output_":"data/ards_dbdata","name":"process/init/relation/ards_dbdata"}
set -xeuo pipefail
cd "$(dirname "$0")"



export DEEPDIVE_CURRENT_PROCESS_NAME='process/init/relation/ards_dbdata'
deepdive create table 'ards_dbdata' && deepdive load 'ards_dbdata'



