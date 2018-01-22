# on xuyang-HP-Pavilion-g4-Notebook-PC: deepdive do sentence
# run/20180122/100339.952233097/plan.sh
# execution plan for data/sentence

: ## process/init/app ##########################################################
: # Done: 2018-01-21T21:48:59+0800 (12h 14m 41s ago)
: process/init/app/run.sh
: mark_done process/init/app
: ##############################################################################


: ## process/init/relation/articles ############################################
: # Done: 2018-01-21T22:13:18+0800 (11h 50m 22s ago)
: process/init/relation/articles/run.sh
: mark_done process/init/relation/articles
: ##############################################################################


: ## data/articles #############################################################
: # Done: 2018-01-21T22:13:18+0800 (11h 50m 22s ago)
: # no-op
: mark_done data/articles
: ##############################################################################


## process/ext_sentence_by_nlp_fenci #########################################
: # Done: 2018-01-22T09:57:11+0800 (6m 29s ago)
# Done: 2018-01-22T09:57:11+0800 (6m 28s ago)
process/ext_sentence_by_nlp_fenci/run.sh
mark_done process/ext_sentence_by_nlp_fenci
##############################################################################


## data/sentence #############################################################
# Done: 2018-01-22T09:57:11+0800 (6m 29s ago)
# no-op
mark_done data/sentence
##############################################################################


