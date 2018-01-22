#!/usr/bin/env python
#encoding:utf-8
from deepdive import *

@tsv_extractor
@returns(lambda
        doc_id=         'text',
        sentence_index= 'text',
        sentence_text=  'text',
        tokens=         'text[]',
        lemmas=         'text[]',
        pos_tags=       'text[]',
        ner_tags=       'text[]',
        doc_offects=    'int[]',
        dep_types=      'text[]',
        dep_tokens=     'int[]',
    :[])
def modify(
    doc_id=         'text',
    sentence_index= 'text',
    sentence_text=  'text',
    tokens=         'text[]',
    lemmas=         'text[]',
    pos_tags=       'text[]',
    ner_tags=       'text[]',
    doc_offsets=    'int[]',
    dep_types=      'text[]',
    dep_tokens=     'int[]'
):
    """Modify the Medicine and ARDs NER POS in sentence"""
    num_tokens = len(tokens)
    #the bad effect we extracted
    ards=['怀孕','皮疹','潮红','胃疼','胃炎','胸口痛','心绞痛',
    '心慌','头疼','胃胀','经期','烧心','胃酸','记忆力减退',
    '四肢无力','浮肿','头晕','心跳过速','缺钙','皮肤长疣',
    '手脚麻','胃病','血压升高','游走性疼痛']
    meds=['优甲乐']

    for ard in ards:
        index=0
        ard_length = len(ard)
        #process every word in the sentence
        while index < num_tokens:
            current_index = index
            word_length=len(tokens[index])
            if word_length < 0:
                continue
            word_pointer=0
            ards_pointer=0
            # compare the char of ard and word in sentence
            # find the first char
            word_pointer_old=0
            for i in range(word_length):
                if tokens[index][i] == ard[0]:
                    word_pointer_old = i
                    word_pointer = i
                    break
            while tokens[index][word_pointer] == ard[ards_pointer]:
                if word_length <= 0:
                    break
                if ards_pointer >= ard_length-1:
                    if word_pointer_old > 0:
                        tokens[current_index-1]+=tokens[current_index][:word_pointer_old]
                        tokens[current_index]=tokens[current_index][word_pointer_old:]
                        lemmas[current_index-1]+=lemmas[current_index][:word_pointer_old]
                        lemmas[current_index]=lemmas[current_index][word_pointer_old:]
                    if word_pointer < word_length-1:
                        print(word_pointer,word_length,tokens[index])
                        tokens[index+1]=tokens[index][word_pointer+1:]+tokens[index+1]
                        tokens[index]=tokens[index][:word_pointer+1]
                    for i in range(current_index,index+1):
                        ner_tags[i]='ARD'
                    break
                if word_pointer+1 < word_length :
                    word_pointer += 1
                    ards_pointer += 1
                else :
                    word_pointer = 0
                    ards_pointer += 1
                    index+=1
                    if index >= num_tokens:
                        break
                    word_length = len(tokens[index])
            index += 1
            if index >= num_tokens:
                break;

    for ard in meds:
        index=0
        ard_length = len(ard)
        #process every word in the sentence
        while index < num_tokens:
            current_index = index
            word_length=len(tokens[index])
            if word_length < 0:
                continue
            word_pointer=0
            ards_pointer=0
            # compare the char of ard and word in sentence
            # find the first char
            word_pointer_old=0
            for i in range(word_length):
                if tokens[index][i] == ard[0]:
                    word_pointer_old = i
                    word_pointer = i
                    break
            while tokens[index][word_pointer] == ard[ards_pointer]:
                if word_length <= 0:
                    break
                if ards_pointer >= ard_length-1:
                    if word_pointer_old > 0:
                        tokens[current_index-1]+=tokens[current_index][:word_pointer_old]
                        tokens[current_index]=tokens[current_index][word_pointer_old:]
                        lemmas[current_index-1]+=lemmas[current_index][:word_pointer_old]
                        lemmas[current_index]=lemmas[current_index][word_pointer_old:]
                    if word_pointer < word_length-1:
                        tokens[index+1]=tokens[index][word_pointer+1:]+tokens[index+1]
                        tokens[index]=tokens[index][:word_pointer+1]
                    for i in range(current_index,index+1):
                        ner_tags[i]='MED'
                    break
                if word_pointer+1 < word_length :
                    word_pointer += 1
                    ards_pointer += 1
                else :
                    index += 1
                    word_length = len(tokens[index])
                    word_pointer = 0
                    ards_pointer += 1
                    if index >= num_tokens:
                        break;
            index += 1


    #calc the doc doc_offects
    doc_offsets[0]=0
    for i in range(1,len(doc_offsets)):
        doc_offsets[i]=doc_offsets[i-1] + len(tokens[i-1])

    yield[
        doc_id,
        sentence_index,
        sentence_text,
        tokens,
        lemmas,
        pos_tags,
        ner_tags,
        doc_offsets,
        dep_types,
        dep_tokens
    ]
