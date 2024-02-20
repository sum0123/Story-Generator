import numpy as np
import pandas as pd
import os
import re
import string
import nltk

# nltk.download("all")
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random



def read_all_stories(story_path):
    txt = []
    for _, _, files in os.walk(story_path):
        for file in files:
            file_path = os.path.join(story_path, file)
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line == "----------":
                        break
                    if line != "":
                        txt.append(line)
    return txt


# stories = read_all_stories(story_path)

def clean_txt(txt):
    cleaned_txt = []
    for line in txt:
        line = line.lower()
        line = re.sub(r"[,.\"\'!@#$%^&*(){}?/;`~:<>+=-\\]", "", line)
        tokens = word_tokenize(line)
        words = [word for word in tokens if word.isalpha()]
        cleaned_txt += words
    return cleaned_txt

