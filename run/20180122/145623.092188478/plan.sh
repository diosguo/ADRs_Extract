# on xuyang-HP-Pavilion-g4-Notebook-PC: deepdive do sentence
# run/20180122/145623.092188478/plan.sh
# execution plan for data/sentence

: ## process/init/app ##########################################################
: # Done: 2018-01-21T21:48:59+0800 (17h 7m 24s ago)
: process/init/app/run.sh
: mark_done process/init/app
: ##############################################################################


: ## process/init/relation/articles ############################################
: # Done: 2018-01-22T11:26:01+0800 (3h 30m 22s ago)
: process/init/relation/articles/run.sh
: mark_done process/init/relation/articles
: ##############################################################################


: ## data/articles #############################################################
: # Done: 2018-01-22T11:26:01+0800 (3h 30m 22s ago)
: # no-op
: mark_done data/articles
: ##############################################################################


## process/ext_sentence_by_nlp_fenci #########################################
# Done: 2018-01-22T11:27:53+0800 (3h 28m 30s ago)
process/ext_sentence_by_nlp_fenci/run.sh
mark_done process/ext_sentence_by_nlp_fenci
##############################################################################


## data/sentence #############################################################
# Done: 2018-01-22T11:27:53+0800 (3h 28m 30s ago)
# no-op
mark_done data/sentence
##############################################################################


