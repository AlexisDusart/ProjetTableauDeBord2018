#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 10:25:40 2018

@author: brandao
"""

import re


def findNumber(text):
    """
        Summary:
            This function is used to find relevent number using the word or
            next or previous (wich are search in list if next or previous
            words are in the list)) 
        In:
            - content extract from an article
        Out:
            - sentences wich contains relevent number in order to analyse
            it and categorize each number in different category
    """
    sentences = []
    text = text.split()
    wPlusOne = ['euros', 'dollars', '$', '€', 'viewers', 'téléspactateurs', 'spectateurs',  ]
    wMinusTwo = ['cashprize', 'salaire', 'cash-prize']
    for i in range(2, len(text)-2):
        if re.findall("\$\d+|\d+\$|\d+€|^\d", text[i]) != []:
            if not re.findall("\$|€", text[i]) and (text[i+1] in wPlusOne or text[i-2] in wMinusTwo):
                under_List = text[i-9:i+9:1]
                chn = " ".join(under_List)
                sentences.append(chn)
            if re.findall("\$|€", text[i]):
                under_List = text[i-9:i+9:1]
                chn = " ".join(under_List)
                sentences.append(chn)
    return sentences
