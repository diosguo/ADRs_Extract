# on xuyang-HP-Pavilion-g4-Notebook-PC: deepdive do sentence
# run/20180122/095705.719252887/plan.sh
# execution plan for data/sentence

: ## process/init/app ##########################################################
: # Done: 2018-01-21T21:48:59+0800 (12h 8m 6s ago)
: process/init/app/run.sh
: mark_done process/init/app
: ##############################################################################


: ## process/init/relation/articles ############################################
: # Done: 2018-01-21T22:13:18+0800 (11h 43m 47s ago)
: process/init/relation/articles/run.sh
: mark_done process/init/relation/articles
: ##############################################################################


: ## data/articles #############################################################
: # Done: 2018-01-21T22:13:18+0800 (11h 43m 47s ago)
: # no-op
: mark_done data/articles
: ##############################################################################


## process/ext_sentence_by_nlp_fenci #########################################
# Done: 2018-01-22T09:55:55+0800 (1m 10s ago)
process/ext_sentence_by_nlp_fenci/run.sh
mark_done process/ext_sentence_by_nlp_fenci
##############################################################################


## data/sentence #############################################################
# Done: 2018-01-22T09:55:55+0800 (1m 10s ago)
# no-op
mark_done data/sentence
##############################################################################


