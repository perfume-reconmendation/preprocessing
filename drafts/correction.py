from multiprocessing import Pool
from spellchecker import SpellChecker
import pandas as pd
import numpy as np

spell = SpellChecker()
cores_to_use = 12


def process(s: pd.Series):
    return s.map(lambda words : [spell.correction(word) for word in words])


def correction(df):

    batch_size = int(len(df['stopwords_removed']) / cores_to_use)
    batch_size * cores_to_use

    batches = [df['stopwords_removed'][i*batch_size:(i+1)*batch_size+cores_to_use] for i in range(0, len(df['stopwords_removed']) - 1)]

    with Pool(cores_to_use) as p:
        batches_return = p.map(process, batches)

    s = pd.Series()
    for batch in batches_return:
        s = s.combine_first(batch)

    spell.correction()

    return s
