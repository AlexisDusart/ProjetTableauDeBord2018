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
from functions.FindNumber import findNumber

import json

path = "/Users/brandao/Desktop/COURS/ProjetTableauDeBord/ProjetTableauDeBord2018/Json"

articles = import_articles(path)
dic_sources = {}
tab_nombres = []
for sources in articles:
    dic_sources[sources] = {}
    with tqdm(desc='Trt', total=len(articles[sources])) as pbar:
        for cle_art in articles[sources]:
            content = cleanhtml(articles[sources][cle_art]['Contenu'])
            title = cleanhtml(articles[sources][cle_art]['Titre'])
            date = articles[sources][cle_art]['Date']
            content_tok = tokeniz(content)
            dic_sources[sources][title] = [handing_entity(content_tok), date]
            tab_nombres.append([findNumber(content), sources, cle_art])
            pbar.update()


def extract_json(Doc_extracted):
    with open('/Users/brandao/Desktop/COURS/ProjetTableauDeBord/ProjetTableauDeBord2018/' + Doc_extracted, 'w') as f:
        json.dump(Doc_extracted, f)


extract_json(dic_sources)
