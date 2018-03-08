#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 10:17:13 2018

@author: brandao
"""
from bs4 import BeautifulSoup
import re

def cleanhtml(contenu):
    """
        Summary:
            this functions clean  html content
        In:
            - text hmtl
        Out:
            - clean text without tags and without html content
    """
    contenu = BeautifulSoup(contenu)
    contenu = contenu.prettify()
    cleanr = re.compile('<.*?>')
    contenu = re.sub(cleanr, '', contenu)
    contenu = contenu.replace("\n", "")
    contenu = " ".join(contenu.split())
    contenu = contenu.replace('(__scads = window.__scads || []).push({\"z\":11865,\"targetId',"")
    contenu = contenu.replace('eSports','eSport')
    contenu = contenu.replace("doubleclickpub('div",'')
    contenu = contenu.replace("LsdException",'')
    contenu = contenu.replace("C’",'')
    contenu = contenu.replace('SemiHidden="true"','')
    contenu = contenu.replace('UnhideWhenUsed="true"','')
    return contenu
