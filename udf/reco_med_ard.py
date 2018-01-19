#!/usr/bin/env python
#encoding:utf-8
from deepdive import *





def ner_ard(doc_id="text", sentence_index="int", sentence_text="text",
        tokens="text[]", lemmas="text[]", pos_tags="text[]", ner_tags="text[]",
        doc_offsets="int[]",dep_types="text[]", dep_token_indexes="int[]",
        medicine_name="text",medicine_name_list="text[]"
        ):
    medicine_name_len = len(medicine_name)
    sentence_text_len = len(sentence_text)
    medicine_name_index = []
    index = 0
    sentence_text_index = 0
    while sentence_text_index < sentence_text_len:
        i = sentence_text_index
        find_index = sentence_text[sentence_text_index:].find(medicine_name)
        if not find_index == -1:
            medicine_start = find_index + i
            sentence_text_index = medicine_start + medicine_name_len
            # if medicine_start==doc_offsets[len(doc_offsets)-1]:
            #     print(medicine_start,doc_offsets[len(doc_offsets)-1])
            #     tokens[index] = medicine_name
            #     lemmas[index] = medicine_name
            #     # 其他先不变
            #     pos_tags[index] = "NN"
            #     ner_tags[index] = "MED"
            #     # dep_types[index] = dep_types[index ]
            #     # dep_token_indexes[index] = dep_token_indexes[index ]
            #     # 将 面 插入
            #     tokens.insert(index + 1, sentence_text[medicine_start + medicine_name_len:len(doc_offsets)])
            #     lemmas.insert(index + 1, sentence_text[medicine_start + medicine_name_len:len(doc_offsets)])
            #     pos_tags.insert(index + 1, "NN")
            #     ner_tags.insert(index + 1, "0")
            #     doc_offsets.insert(index + 1, medicine_start + medicine_name_len)
            #     dep_types.insert(index + 1, "dep")
            #     dep_token_indexes.insert(index + 1, "0")
            # print(sentence_text_index)
            for index in range(len(doc_offsets) - 1):
                # print(index,medicine_start)
                if doc_offsets[index] == medicine_start:
                    # 当开头正好匹配
                    # print(doc_offsets[index+1], medicine_start+medicine_name_len)
                    if doc_offsets[index + 1] == medicine_start + medicine_name_len:
                        # 当结尾正好匹配，全部识别正确只把NER改为MED即可，MED代表实体药
                        ner_tags[index] = "MED"
                        break
                    elif doc_offsets[index + 1] < medicine_start + medicine_name_len:
                        # 开头正好匹配，后面不能正确匹配
                        skewing = 0
                        while doc_offsets[index + skewing] < medicine_start + medicine_name_len:
                            skewing += 1
                        # print(doc_offsets[index+skewing],medicine_start+medicine_name_len)
                        if doc_offsets[index + skewing] == medicine_start + medicine_name_len:
                            # 优甲乐药片 优甲 乐 药片 面粉
                            tokens[index] = medicine_name
                            lemmas[index] = medicine_name
                            # 词性标注，命名实体识别先以以后面的为准
                            pos_tags[index] = "NN"
                            ner_tags[index] = "MED"
                            dep_types[index] = dep_types[index + skewing - 1]
                            dep_token_indexes[index] = dep_token_indexes[index + skewing - 1]
                            for x in range(skewing - 1):
                                del pos_tags[index + 1]
                                del tokens[index + 1]
                                del lemmas[index + 1]
                                del ner_tags[index + 1]
                                del dep_token_indexes[index + 1]
                                del dep_types[index + 1]
                                del doc_offsets[index + 1]
                            # print(11111)
                            # print(tokens,pos_tags,ner_tags,doc_offsets,dep_token_indexes,dep_types,doc_offsets)
                            break
                        else:
                            # 优甲乐药片 优甲 乐 药 片面 粉
                            tokens[index] = medicine_name
                            lemmas[index] = medicine_name
                            pos_tags[index] = "NN"
                            ner_tags[index] = "MED"
                            # dep_types[index] = dep_types[index + skewing - 2]
                            # dep_token_indexes[index] = dep_token_indexes[index + skewing - 2]
                            tokens[index + skewing - 1] = sentence_text[medicine_start + medicine_name_len:doc_offsets[
                                index + skewing]]
                            lemmas[index + skewing - 1] = sentence_text[medicine_start + medicine_name_len:doc_offsets[
                                index + skewing]]
                            # print(sentence_text[medicine_start+medicine_name_len:doc_offsets[index+skewing]])
                            # pos_tags[index+skewing-1] = pos_tags[index + skewing - 1]
                            # ner_tags[index+skewing-1] = ner_tags[index + skewing - 1]
                            # dep_types[index+skewing-1] = dep_types[index + skewing - 1]
                            # dep_token_indexes[index+skewing-1] = dep_token_indexes[index + skewing - 1]
                            for x in range(skewing - 2):
                                del pos_tags[index + 1]
                                del tokens[index + 1]
                                del lemmas[index + 1]
                                del ner_tags[index + 1]
                                del dep_token_indexes[index + 1]
                                del dep_types[index + 1]
                                del doc_offsets[index + 1]
                            break
                    elif doc_offsets[index + 1] > medicine_start + medicine_name_len:
                        # 优甲乐药片 优甲乐药片面 粉
                        tokens[index] = medicine_name
                        lemmas[index] = medicine_name
                        # 其他先不变
                        pos_tags[index] = "NN"
                        ner_tags[index] = "MED"
                        # dep_types[index] = dep_types[index ]
                        # dep_token_indexes[index] = dep_token_indexes[index ]
                        # 将 面 插入
                        tokens.insert(index + 1,
                                      sentence_text[medicine_start + medicine_name_len:doc_offsets[index + 1]])
                        lemmas.insert(index + 1,
                                      sentence_text[medicine_start + medicine_name_len:doc_offsets[index + 1]])
                        pos_tags.insert(index + 1, "NN")
                        ner_tags.insert(index + 1, "0")
                        doc_offsets.insert(index + 1, medicine_start + medicine_name_len)
                        dep_types.insert(index + 1, "dep")
                        dep_token_indexes.insert(index + 1, 0)
                        break
                elif doc_offsets[index] < medicine_start and doc_offsets[index + 1] > medicine_start:  # 药名识别时被分开，进行合并操作
                    if doc_offsets[index + 1] == medicine_start + medicine_name_len:
                        # 良优甲乐药片 面粉
                        tokens[index] = sentence_text[index:medicine_start]
                        lemmas[index] = sentence_text[index:medicine_start]
                        pos_tags[index] = "NN"
                        ner_tags[index] = "O"
                        # dep_types[index] = dep_types[index + skewing - 2]
                        # dep_token_indexes[index] = dep_token_indexes[index + skewing - 2]
                        tokens.insert(index + 1, medicine_name)
                        lemmas.insert(index + 1, medicine_name)
                        pos_tags.insert(index + 1, "NN")
                        ner_tags.insert(index + 1, "MED")
                        doc_offsets.insert(index + 1, medicine_start)
                        dep_types.insert(index + 1, "")
                        dep_token_indexes.insert(index + 1, medicine_start)
                        break
                    elif doc_offsets[index + 1] < medicine_start + medicine_name_len:
                        skewing = 0
                        while doc_offsets[index + skewing] < medicine_start + medicine_name_len:
                            skewing += 1
                        # print(doc_offsets[index+skewing],medicine_start+medicine_name_len)
                        if doc_offsets[index + skewing] == medicine_start + medicine_name_len:
                            # 优甲乐药片 良优甲 乐 药片面粉
                            tokens[index] = sentence_text[index:medicine_start]
                            lemmas[index] = sentence_text[index:medicine_start]
                            pos_tags[index] = "NN"
                            ner_tags[index] = "O"
                            # dep_types[index] = dep_types[index + skewing - 2]
                            # dep_token_indexes[index] = dep_token_indexes[index + skewing - 2]
                            tokens.insert(index + 1, medicine_name)
                            lemmas.insert(index + 1, medicine_name)
                            pos_tags.insert(index + 1, "NN")
                            ner_tags.insert(index + 1, "MED")
                            doc_offsets.insert(index + 1, medicine_start)
                            dep_types.insert(index + 1, "")
                            dep_token_indexes.insert(index + 1, medicine_start)
                            for x in range(skewing - 1):
                                del pos_tags[index + 2]
                                del tokens[index + 2]
                                del lemmas[index + 2]
                                del ner_tags[index + 2]
                                del dep_token_indexes[index + 2]
                                del dep_types[index + 2]
                                del doc_offsets[index + 2]
                            # print(11111)
                            # print(tokens, pos_tags, ner_tags, doc_offsets, dep_token_indexes, dep_types, doc_offsets)
                            break
                        else:
                            # 优甲乐药片 良优甲 乐 药 片面 粉
                            tokens[index] = sentence_text[index:medicine_start]
                            lemmas[index] = sentence_text[index:medicine_start]
                            pos_tags[index] = "NN"
                            ner_tags[index] = "O"
                            # print("aaa")
                            # dep_types[index] = dep_types[index + skewing - 2]
                            # dep_token_indexes[index] = dep_token_indexes[index + skewing - 2]
                            tokens.insert(index + 1, medicine_name)
                            lemmas.insert(index + 1, medicine_name)
                            pos_tags.insert(index + 1, "NN")
                            ner_tags.insert(index + 1, "MED")
                            doc_offsets.insert(index + 1, medicine_start)
                            dep_types.insert(index + 1, "")
                            dep_token_indexes.insert(index + 1, medicine_start)
                            tokens[index + skewing] = sentence_text[medicine_start + medicine_name_len:doc_offsets[
                                index + skewing + 1]]
                            lemmas[index + skewing] = sentence_text[medicine_start + medicine_name_len:doc_offsets[
                                index + skewing + 1]]
                            # print(sentence_text[medicine_start + medicine_name_len:doc_offsets[index + skewing]])
                            # pos_tags[index+skewing-1] = pos_tags[index + skewing - 1]
                            # ner_tags[index+skewing-1] = ner_tags[index + skewing - 1]
                            # dep_types[index+skewing-1] = dep_types[index + skewing - 1]
                            # dep_token_indexes[index+skewing-1] = dep_token_indexes[index + skewing - 1]
                            # print(sentence_text[medicine_start + medicine_name_len:doc_offsets[index + skewing]])
                            # pos_tags[index+skewing-1] = pos_tags[index + skewing - 1]
                            # ner_tags[index+skewing-1] = ner_tags[index + skewing - 1]
                            # dep_types[index+skewing-1] = dep_types[index + skewing - 1]
                            # dep_token_indexes[index+skewing-1] = dep_token_indexes[index + skewing - 1]
                            for x in range(skewing - 2):
                                del pos_tags[index + 2]
                                del tokens[index + 2]
                                del lemmas[index + 2]
                                del ner_tags[index + 2]
                                del dep_token_indexes[index + 2]
                                del dep_types[index + 2]
                                del doc_offsets[index + 2]
                            break
                    elif doc_offsets[index + 1] > medicine_start + medicine_name_len:
                        tokens[index] = sentence_text[index:medicine_start]
                        lemmas[index] = sentence_text[index:medicine_start]
                        pos_tags[index] = "NN"
                        ner_tags[index] = "O"
                        # dep_types[index] = dep_types[index + skewing - 2]
                        # dep_token_indexes[index] = dep_token_indexes[index + skewing - 2]
                        tokens.insert(index + 1, medicine_name)
                        lemmas.insert(index + 1, medicine_name)
                        pos_tags.insert(index + 1, "NN")
                        ner_tags.insert(index + 1, "MED")
                        doc_offsets.insert(index + 1, medicine_start)
                        dep_types.insert(index + 1, "")
                        dep_token_indexes.insert(index + 1, medicine_start)
                        tokens.insert(index + 2,
                                      sentence_text[medicine_start + medicine_name_len:doc_offsets[index + 2]])
                        lemmas.insert(index + 2,
                                      sentence_text[medicine_start + medicine_name_len:doc_offsets[index + 2]])
                        pos_tags.insert(index + 2, "NN")
                        ner_tags.insert(index + 2, "0")
                        doc_offsets.insert(index + 2, medicine_start + medicine_name_len)
                        dep_types.insert(index + 2, "dep")
                        dep_token_indexes.insert(index + 2,0)
                        break
                index += 1
        sentence_text_index += 1
    for medicine_name in medicine_name_list:
        medicine_name_len = len(medicine_name)
        sentence_text_len = len(sentence_text)
        medicine_name_index = []
        index = 0
        sentence_text_index = 0
        while sentence_text_index < sentence_text_len:
            i = sentence_text_index
            find_index = sentence_text[sentence_text_index:].find(medicine_name)
            # print(sentence_text_index)
            if not find_index == -1:
                medicine_start = find_index + i
                sentence_text_index = medicine_start + medicine_name_len
                # if medicine_start == doc_offsets[-1]:
                #     tokens[index] = medicine_name
                #     lemmas[index] = medicine_name
                #     # 其他先不变
                #     pos_tags[index] = "NN"
                #     ner_tags[index] = "ARD"
                #     # dep_types[index] = dep_types[index ]
                #     # dep_token_indexes[index] = dep_token_indexes[index ]
                #     # 将 面 插入
                #     tokens.insert(index + 1, sentence_text[medicine_start + medicine_name_len:len(doc_offsets)])
                #     lemmas.insert(index + 1, sentence_text[medicine_start + medicine_name_len:len(doc_offsets)])
                #     pos_tags.insert(index + 1, "NN")
                #     ner_tags.insert(index + 1, "0")
                #     doc_offsets.insert(index + 1, medicine_start + medicine_name_len)
                #     dep_types.insert(index + 1, "dep")
                #     dep_token_indexes.insert(index + 1, "0")
                # print(sentence_text_index)
                for index in range(len(doc_offsets)-1):
                    # print(index,medicine_start)
                    if doc_offsets[index] == medicine_start:
                        # 当开头正好匹配
                        # print(doc_offsets[index+1], medicine_start+medicine_name_len)
                        if doc_offsets[index + 1] == medicine_start + medicine_name_len:
                            # 当结尾正好匹配，全部识别正确只把NER改为MED即可，MED代表实体药
                            ner_tags[index] = "ARD"
                            break
                        elif doc_offsets[index + 1] < medicine_start + medicine_name_len:
                            # 开头正好匹配，后面不能正确匹配
                            skewing = 0

                            while doc_offsets[index + skewing] < medicine_start + medicine_name_len:
                                if index+skewing+1<len(doc_offsets):
                                    skewing += 1
                                else:
                                    break
                            # print(doc_offsets[index+skewing],medicine_start+medicine_name_len)
                            if doc_offsets[index + skewing] == medicine_start + medicine_name_len:
                                # 优甲乐药片 优甲 乐 药片 面粉
                                tokens[index] = medicine_name
                                lemmas[index] = medicine_name
                                # 词性标注，命名实体识别先以以后面的为准
                                pos_tags[index] = "NN"
                                ner_tags[index] = "ARD"
                                dep_types[index] = dep_types[index + skewing - 1]
                                dep_token_indexes[index] = dep_token_indexes[index + skewing - 1]
                                for x in range(skewing - 1):
                                    del pos_tags[index + 1]
                                    del tokens[index + 1]
                                    del lemmas[index + 1]
                                    del ner_tags[index + 1]
                                    del dep_token_indexes[index + 1]
                                    del dep_types[index + 1]
                                    del doc_offsets[index + 1]
                                # print(11111)
                                # print(tokens,pos_tags,ner_tags,doc_offsets,dep_token_indexes,dep_types,doc_offsets)
                                break
                            else:
                                # 优甲乐药片 优甲 乐 药 片面 粉
                                tokens[index] = medicine_name
                                lemmas[index] = medicine_name
                                pos_tags[index] = "NN"
                                ner_tags[index] = "ARD"
                                # dep_types[index] = dep_types[index + skewing - 2]
                                # dep_token_indexes[index] = dep_token_indexes[index + skewing - 2]
                                tokens[index + skewing - 1] = sentence_text[
                                                              medicine_start + medicine_name_len:doc_offsets[
                                                                  index + skewing]]
                                lemmas[index + skewing - 1] = sentence_text[
                                                              medicine_start + medicine_name_len:doc_offsets[
                                                                  index + skewing]]
                                # print(sentence_text[medicine_start+medicine_name_len:doc_offsets[index+skewing]])
                                # pos_tags[index+skewing-1] = pos_tags[index + skewing - 1]
                                # ner_tags[index+skewing-1] = ner_tags[index + skewing - 1]
                                # dep_types[index+skewing-1] = dep_types[index + skewing - 1]
                                # dep_token_indexes[index+skewing-1] = dep_token_indexes[index + skewing - 1]
                                for x in range(skewing - 2):
                                    del pos_tags[index + 1]
                                    del tokens[index + 1]
                                    del lemmas[index + 1]
                                    del ner_tags[index + 1]
                                    del dep_token_indexes[index + 1]
                                    del dep_types[index + 1]
                                    del doc_offsets[index + 1]
                                break
                        elif doc_offsets[index + 1] > medicine_start + medicine_name_len:
                            # 优甲乐药片 优甲乐药片面 粉
                            tokens[index] = medicine_name
                            lemmas[index] = medicine_name
                            # 其他先不变
                            pos_tags[index] = "NN"
                            ner_tags[index] = "ARD"
                            # dep_types[index] = dep_types[index ]
                            # dep_token_indexes[index] = dep_token_indexes[index ]
                            # 将 面 插入
                            tokens.insert(index + 1,
                                          sentence_text[medicine_start + medicine_name_len:doc_offsets[index + 1]])
                            lemmas.insert(index + 1,
                                          sentence_text[medicine_start + medicine_name_len:doc_offsets[index + 1]])
                            pos_tags.insert(index + 1, "NN")
                            ner_tags.insert(index + 1, "0")
                            doc_offsets.insert(index + 1, medicine_start + medicine_name_len)
                            dep_types.insert(index + 1, "dep")
                            dep_token_indexes.insert(index + 1, 0)
                            break
                    elif doc_offsets[index] < medicine_start and doc_offsets[
                        index + 1] > medicine_start:  # 药名识别时被分开，进行合并操作
                        if doc_offsets[index + 1] == medicine_start + medicine_name_len:
                            # 良优甲乐药片 面粉
                            tokens[index] = sentence_text[index:medicine_start]
                            lemmas[index] = sentence_text[index:medicine_start]
                            pos_tags[index] = "NN"
                            ner_tags[index] = "O"
                            # dep_types[index] = dep_types[index + skewing - 2]
                            # dep_token_indexes[index] = dep_token_indexes[index + skewing - 2]
                            tokens.insert(index + 1, medicine_name)
                            lemmas.insert(index + 1, medicine_name)
                            pos_tags.insert(index + 1, "NN")
                            ner_tags.insert(index + 1, "ARD")
                            doc_offsets.insert(index + 1, medicine_start)
                            dep_types.insert(index + 1, "")
                            dep_token_indexes.insert(index + 1, medicine_start)
                            break
                        elif doc_offsets[index + 1] < medicine_start + medicine_name_len:
                            skewing = 0
                            while doc_offsets[index + skewing] < medicine_start + medicine_name_len:
                                skewing += 1
                            # print(doc_offsets[index+skewing],medicine_start+medicine_name_len)
                            if doc_offsets[index + skewing] == medicine_start + medicine_name_len:
                                # 优甲乐药片 良优甲 乐 药片面粉
                                tokens[index] = sentence_text[index:medicine_start]
                                lemmas[index] = sentence_text[index:medicine_start]
                                pos_tags[index] = "NN"
                                ner_tags[index] = "O"
                                # dep_types[index] = dep_types[index + skewing - 2]
                                # dep_token_indexes[index] = dep_token_indexes[index + skewing - 2]
                                tokens.insert(index + 1, medicine_name)
                                lemmas.insert(index + 1, medicine_name)
                                pos_tags.insert(index + 1, "NN")
                                ner_tags.insert(index + 1, "ARD")
                                doc_offsets.insert(index + 1, medicine_start)
                                dep_types.insert(index + 1, "dep")
                                dep_token_indexes.insert(index + 1, medicine_start)
                                for x in range(skewing - 1):
                                    del pos_tags[index + 2]
                                    del tokens[index + 2]
                                    del lemmas[index + 2]
                                    del ner_tags[index + 2]
                                    del dep_token_indexes[index + 2]
                                    del dep_types[index + 2]
                                    del doc_offsets[index + 2]
                                # print(11111)
                                # print(tokens, pos_tags, ner_tags, doc_offsets, dep_token_indexes, dep_types, doc_offsets)
                                break
                            else:
                                # 优甲乐药片 良优甲 乐 药 片面 粉
                                tokens[index] = sentence_text[index:medicine_start]
                                lemmas[index] = sentence_text[index:medicine_start]
                                pos_tags[index] = "NN"
                                ner_tags[index] = "O"
                                # print("aaa")
                                # dep_types[index] = dep_types[index + skewing - 2]
                                # dep_token_indexes[index] = dep_token_indexes[index + skewing - 2]
                                tokens.insert(index + 1, medicine_name)
                                lemmas.insert(index + 1, medicine_name)
                                pos_tags.insert(index + 1, "NN")
                                ner_tags.insert(index + 1, "ARD")
                                doc_offsets.insert(index + 1, medicine_start)
                                dep_types.insert(index + 1, "dep")
                                dep_token_indexes.insert(index + 1, medicine_start)
                                tokens[index + skewing] = sentence_text[medicine_start + medicine_name_len:doc_offsets[
                                    index + skewing + 1]]
                                lemmas[index + skewing] = sentence_text[medicine_start + medicine_name_len:doc_offsets[
                                    index + skewing + 1]]
                                # print(sentence_text[medicine_start + medicine_name_len:doc_offsets[index + skewing]])
                                # pos_tags[index+skewing-1] = pos_tags[index + skewing - 1]
                                # ner_tags[index+skewing-1] = ner_tags[index + skewing - 1]
                                # dep_types[index+skewing-1] = dep_types[index + skewing - 1]
                                # dep_token_indexes[index+skewing-1] = dep_token_indexes[index + skewing - 1]
                                # print(sentence_text[medicine_start + medicine_name_len:doc_offsets[index + skewing]])
                                # pos_tags[index+skewing-1] = pos_tags[index + skewing - 1]
                                # ner_tags[index+skewing-1] = ner_tags[index + skewing - 1]
                                # dep_types[index+skewing-1] = dep_types[index + skewing - 1]
                                # dep_token_indexes[index+skewing-1] = dep_token_indexes[index + skewing - 1]
                                for x in range(skewing - 2):
                                    del pos_tags[index + 2]
                                    del tokens[index + 2]
                                    del lemmas[index + 2]
                                    del ner_tags[index + 2]
                                    del dep_token_indexes[index + 2]
                                    del dep_types[index + 2]
                                    del doc_offsets[index + 2]
                                break
                        elif doc_offsets[index + 1] > medicine_start + medicine_name_len:
                            tokens[index] = sentence_text[index:medicine_start]
                            lemmas[index] = sentence_text[index:medicine_start]
                            pos_tags[index] = "NN"
                            ner_tags[index] = "O"
                            # dep_types[index] = dep_types[index + skewing - 2]
                            # dep_token_indexes[index] = dep_token_indexes[index + skewing - 2]
                            tokens.insert(index + 1, medicine_name)
                            lemmas.insert(index + 1, medicine_name)
                            pos_tags.insert(index + 1, "NN")
                            ner_tags.insert(index + 1, "ARD")
                            doc_offsets.insert(index + 1, medicine_start)
                            dep_types.insert(index + 1, "dep")
                            dep_token_indexes.insert(index + 1, medicine_start)
                            tokens.insert(index + 2,
                                          sentence_text[medicine_start + medicine_name_len:doc_offsets[index + 2]])
                            lemmas.insert(index + 2,
                                          sentence_text[medicine_start + medicine_name_len:doc_offsets[index + 2]])
                            pos_tags.insert(index + 2, "NN")
                            ner_tags.insert(index + 2, "0")
                            doc_offsets.insert(index + 2, medicine_start + medicine_name_len)
                            dep_types.insert(index + 2, "dep")
                            dep_token_indexes.insert(index + 2, 0)
                            break
                    index += 1
            sentence_text_index += 1

    return [doc_id,sentence_index,sentence_text,tokens,lemmas,pos_tags,ner_tags,doc_offsets,dep_types,dep_token_indexes]


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
    num_tokens = len(ner_tags)
    #the bad effect we extracted
    ards=['怀孕','皮疹','潮红','胃疼','胃炎','胸口痛','心绞痛',
    '心慌','头疼','胃胀','经期','烧心','胃酸','记忆力减退',
    '四肢无力','浮肿','头晕','心跳过速','缺钙','皮肤长疣',
    '手脚麻','胃病','血压升高']
    medicine='优甲乐'
    res = ner_ard(doc_id,sentence_index,sentence_text,tokens,lemmas, pos_tags,
                ner_tags,doc_offsets,dep_types,dep_token_indexes,medicine,ards)

    yield res
