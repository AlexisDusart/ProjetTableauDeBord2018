#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 08:07:44 2018

@author: brandao
"""

from functions.import_json import import_articles
from functions.tokenize import tokeniz
from functions.named_entity import handing_entity
from functions.cleanhtml import cleanhtml

import operator


path = "/Users/brandao/Desktop/COURS/ProjetTableauDeBord/ProjetTableauDeBord2018/Json"

articles = import_articles(path)
tab_ent = []
for sources in articles:
    with tqdm(desc='JSONing', total=len(articles)) as pbar:
    for cle_art in articles[sources]:
            content = cleanhtml(articles[sources][cle_art]['Contenu'])
            title = cleanhtml(articles[sources][cle_art]['Titre'])
            content_tok = tokeniz(content)
            entity = handing_entity(sources, title, content_tok, tab_ent)
            pbar.update()

ent_text = []
i=0
for elemnt in tab_ent:
    ent_text.append(elemnt[2])
    
compte = {}.fromkeys(set(ent_text),0)
for valeur in ent_text:
    compte[valeur] += 1
    
sorted_compte = sorted(compte.items(), key=operator.itemgetter(1), reverse = True)
