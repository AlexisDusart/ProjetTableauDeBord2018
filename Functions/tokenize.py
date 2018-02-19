#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 10:40:13 2018

@author: brandao
"""

import spacy
nlp = spacy.load('fr')


def tokeniz(text):  # Tokenize a text with library Spacy
    """
        Summary: Transorm all the text  where each word become tokens
        tokens
        In:
            - article: content of the article
        Out:
            - tokenize article, each word is a token which we can apply some
            functions as .text, . lemma etc ...
    """
    simple_art = text.replace("'", " ")
    doc = nlp(simple_art)
    return doc