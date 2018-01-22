#!/usr/bin/env bash
# cmd_extractor  process/init/relation/articles
# {"style":"cmd_extractor","cmd":"deepdive create table 'articles' && deepdive load 'articles'","dependencies_":["process/init/app"],"output_relation":"articles","output_":"data/articles","name":"process/init/relation/articles"}
set -xeuo pipefail
cd "$(dirname "$0")"



export DEEPDIVE_CURRENT_PROCESS_NAME='process/init/relation/articles'
deepdive create table 'articles' && deepdive load 'articles'



