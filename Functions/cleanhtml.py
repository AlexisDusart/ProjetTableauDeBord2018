#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 10:17:13 2018

@author: brandao
"""

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
    return contenu