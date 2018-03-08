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
dic_sources = {}
for sources in articles:
    dic_sources[sources] = {}
    with tqdm(desc='JSONing', total=len(articles[sources])) as pbar:
        for cle_art in articles[sources]:
            content = cleanhtml(articles[sources][cle_art]['Contenu'])
            title = cleanhtml(articles[sources][cle_art]['Titre'])
            date = articles[sources][cle_art]['Date']
            content_tok = tokeniz(content)
            dic_sources[sources][title] = handing_entity(content_tok)
#            entity = handing_entity(sources, title, date, content_tok, tab_ent)
            pbar.update()

dicdic = {}
dicdic['blabla'] = {}
dicdic['blabla']['roro'] = 4
dicdic['blabla']['rara'] = 4



ent_text = []
i=0
for elemnt in tab_ent:
    ent_text.append(elemnt[2])
    
compte = {}.fromkeys(set(ent_text),0)
for valeur in ent_text:
    compte[valeur] += 1
    
sorted_compte = sorted(compte.items(), key=operator.itemgetter(1), reverse = True)

with open('/Users/brandao/Desktop/COURS/ProjetTableauDeBord/ProjetTableauDeBord2018/entity.json', 'w') as f:
     json.dump(entity, f)