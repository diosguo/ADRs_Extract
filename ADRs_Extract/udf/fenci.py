#!/usr/bin/env python
#encoding:utf-8
from deepdive import *
import jieba
import jieba.posseg as pseg
import jieba.analyse


@tsv_extractor
@returns(lambda
        doc_id=         'text',
        sentence_index= 'int',
        sentence_text=  'text',
        tokens=         'text[]',
        lemmas=         'text[]',
        pos_tags=       'text[]',
        ner_tags=       'text[]',
        doc_offects=    'int[]',
        dep_types=      'text[]',
        dep_tokens=     'int[]',
    :[])
def extract(
    doc_id='text',
    content='text',
):
    jieba.load_userdict('/home/xuyang/Projects/ADR2/udf/dict.txt')
    cutlist='@@@'
    sent_list=content.split(cutlist)
    #process the '。'
    #for in for is too slow
    new_sent=[]
    for sent in sent_list:
        new_sent.extend(sent.split('。'))
    sent_list=new_sent
    new_sent=[]
    for sent in sent_list:
        new_sent.extend(sent.split('？'))
    sent_list=new_sent
    new_sent=[]
    for sent in sent_list:
        new_sent.extend(sent.split('！'))


    for index,sent in enumerate(new_sent):
        if sent=='' or sent==' ' :
            del new_sent[index]

    # file=open('/home/xuyang/fenci.txt','a')
    # pos=open('/home/xuyang/pos.txt','a')
    for index,sentence in enumerate(new_sent):
        tokens=[]
        pos_tags=[]
        doc_offects=[]
        dep_tokens=[]
        word_list=pseg.cut(sentence)
        for w in word_list:
            tokens.append(w.word.encode('utf-8'))
            pos_tags.append(w.flag.encode('utf-8'))
            doc_offects.append(1)
            dep_tokens.append(2)
        file=open('/home/xuyang/fenci.txt','a')
        pos=open('/home/xuyang/pos.txt','a')
        file.write(doc_id+','+str(index)+','+' '.join(tokens)+'\n')
        pos.write(doc_id+','+str(index)+','+' '.join(pos_tags)+'\n')
        file.close()
        pos.close()
        yield [
            doc_id,
            index+1,
            sentence,
            tokens,
            tokens,
            pos_tags,
            tokens,
            doc_offects,
            tokens,
            dep_tokens,
        ]
