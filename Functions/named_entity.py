#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 10:59:32 2018

@author: brandao
"""


def handing_entity(tokenize_text):
    """
        Summary:
            we go through a tokenize text (result of the function "tokenize"),
            to find named entity in the text.
        In:
            - tokenize text, result of function "tokeniz()"
        Out:
            - list of named entity, and the same list, but whitespaces
            are replace by _, in order to recognize one entity, as one token in
            the lemmatisation
    """
    tab = []
    for entity in tokenize_text.ents:
        tab.append([entity.text, entity.label_])
#        tab_entity.append([source, title, date, entity.text, entity.label_])
    return tab
