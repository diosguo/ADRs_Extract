# on xuyang-HP-Pavilion-g4-Notebook-PC: deepdive do sentence
# run/20180122/154842.825974346/plan.sh
# execution plan for data/sentence

: ## process/init/app ##########################################################
: # Done: 2018-01-21T21:48:59+0800 (17h 59m 43s ago)
: process/init/app/run.sh
: mark_done process/init/app
: ##############################################################################


: ## process/init/relation/articles ############################################
: # Done: 2018-01-22T11:26:01+0800 (4h 22m 41s ago)
: process/init/relation/articles/run.sh
: mark_done process/init/relation/articles
: ##############################################################################


: ## data/articles #############################################################
: # Done: 2018-01-22T11:26:01+0800 (4h 22m 41s ago)
: # no-op
: mark_done data/articles
: ##############################################################################


## process/ext_sentence_by_nlp_fenci #########################################
# Done: 2018-01-22T15:44:24+0800 (4m 18s ago)
process/ext_sentence_by_nlp_fenci/run.sh
mark_done process/ext_sentence_by_nlp_fenci
##############################################################################


## data/sentence #############################################################
# Done: 2018-01-22T15:44:24+0800 (4m 18s ago)
# no-op
mark_done data/sentence
##############################################################################


