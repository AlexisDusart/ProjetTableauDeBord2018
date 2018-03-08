#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 10:46:04 2018

@author: brandao
"""

from os import listdir
import json
from tqdm import tqdm

def import_articles(path_source):
    """
        Summary:
            Import a panel of article from robot group (g4) according to the
            server structure :
                [date] / path_source / newspaper / article
            where "date" corresponds to the most recent repository.
        In:
            - path_source : a string which corresponds to the localisation
                 of robot group (g4)
        Out:
            - articles : a dict of articles
    """
    # Initialisation
    article = {}

    sources = listdir(path_source)
    # Loop: For each inewspaper
    for js in sources:
        # management of hidden repositories: required on macOS (.ds_store)
        if not js.startswith('.'):
            xdirpaper = path_source + '/' + js
            # progress bar for each newspaper repository
            with tqdm(desc=str(sources), total=len(sources)) as fbar:
                with open(xdirpaper, 'r',
                          encoding='utf-8') as dict_robot:
                    article[js] = json.load(dict_robot)
                fbar.update()
                continue
            # End newspaper repository
        continue
    # End all newspapers
    return article

