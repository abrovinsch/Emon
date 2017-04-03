#!/usr/bin/python
# -*- coding: utf-8 -*-

from pathlib import Path


inflections = list()

def load_inflections(lang):

    source_file_path = "inflections/inflections_"+lang+".csv"
    
    #source_file_path = "words.txt"
    sfp = Path(source_file_path)
    
    if not sfp.is_file():
        print("Couldn't find inflections for language: " + lang + "(" + source_file_path + ")")
        return
    
    sourcefile = open(source_file_path)
    contents = sourcefile.read()
    sourcefile.close()
    
    inflections = list()
    
    for lines in contents.split("\n"):
        inflections_group = list()
        
        for item in lines.split(";"):
            if not item in inflections_group:
               inflections_group.append(item)
        inflections.append(inflections_group)
        
    return inflections

def get_inflections_for(word, inflections):
    
    for inflection in inflections :
        if word in inflection:
            return inflection
    
print(get_inflections_for("sleep",load_inflections("en")))