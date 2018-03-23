#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 10:25:40 2018

@author: brandao
"""

import re


def findNumber(texte):
    phrases = []
    texte = texte.split()
    motPlusUn = ['euros', 'dollars', '$', '€', 'viewers', 'téléspactateurs', 'spectateurs',  ]
    motMoinsDeux = ['cashprize', 'salaire', 'cash-prize']
    for i in range(2, len(texte)-2):
        if re.findall("\$\d+|\d+\$|\d+€|^\d", texte[i]) != []:
            if not re.findall("\$|€", texte[i]) and (texte[i+1] in motPlusUn or texte[i-2] in motMoinsDeux):
                sousList = texte[i-9:i+9:1]
                chn = " ".join(sousList)
                phrases.append(chn)
            if re.findall("\$|€", texte[i]):
                sousList = texte[i-9:i+9:1]
                chn = " ".join(sousList)
                phrases.append(chn)
    return phrases
