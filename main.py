#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 08:07:44 2018

@author: brandao
"""
~
from functions.import_json import import_articles
from functions.tokenize import tokeniz
from functions.named_entity import handing_entity
from functions.cleanhtml import cleanhtml

import operator


path = "/Users/brandao/Desktop/COURS/ProjetTableauDeBord/ProjetTableauDeBord2018/Json"

articles = import_articles(path)
dic_sources = {}
tab_nombres = []
for sources in articles:
    dic_sources[sources] = {}
    with tqdm(desc='JSONing', total=len(articles[sources])) as pbar:
        for cle_art in articles[sources]:
            content = cleanhtml(articles[sources][cle_art]['Contenu'])
            title = cleanhtml(articles[sources][cle_art]['Titre'])
            date = articles[sources][cle_art]['Date']
           content_tok = tokeniz(content)
            dic_sources[sources][title] = [handing_entity(content_tok), date]
            entity = handing_entity(sources, title, date, content_tok, tab_ent)
            tab_nombres.append([findNumber(content), sources, cle_art])
            pbar.update()


for i in range(len(tab_nombres)):
    if not tab_nombres[i][0]:
        del tab_nombres[i]

        
tab_nombres[0][0]
tab_nombres[0]
text = cleanhtml(articles['esportsBFM.json']['0']['Contenu'])
text
ent_text = []
i=0
for elemnt in tab_ent:
    ent_text.append(elemnt[3])
    
compte = {}.fromkeys(set(ent_text),0)
for valeur in ent_text:
    compte[valeur] += 1
    
sorted_compte = sorted(compte.items(), key=operator.itemgetter(1), reverse = True)

with open('/Users/brandao/Desktop/COURS/ProjetTableauDeBord/ProjetTableauDeBord2018/Trt_nombres.json', 'w') as f:
     json.dump(Trt_nombres, f)