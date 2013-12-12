# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import sys
import os
import csv
import json

import numpy as np
import pandas as pd

from libshorttext.converter import Text2svmConverter, FeatureGenerator, TextPreprocessor, convert_text
from libshorttext.classifier import train_converted_text

# <codecell>

project_name = 'crp_expenditures_nov4_7-16'

# <codecell>

!tree

# <codecell>

BASE_DIR = '/home/blannon/Dropbox/dev/experiments/CRP-expenditures_libshorttext/'

CONVERTER_DIR = os.path.join(BASE_DIR, 'converters')

DATA_DIR = os.path.join(BASE_DIR, 'data')
CLEAN_DIR = os.path.join(DATA_DIR, 'clean')
TRAIN_DIR = os.path.join(DATA_DIR, 'labeled', 'train')
TEST_DIR = os.path.join(DATA_DIR, 'labeled', 'test')

train_csv = os.path.join(CLEAN_DIR, project_name + '_train.csv')
test_csv = os.path.join(CLEAN_DIR, project_name + '_test.csv')

train_svm = os.path.join(TRAIN_DIR, project_name + '_train.svm')
test_svm = os.path.join(TEST_DIR, project_name + '_test.svm')

MODELS_DIR = os.path.join(BASE_DIR, 'models')

# <codecell>

settings = {}

# STEMMING: 1 to use porter, 0 for no stemming, or give your 
#           own stemmer that maps from a list of tokens to a 
#           list of stemmed tokens
settings['stemming'] = '1'

# STOPWORDS: 1 to use default stops, 0 for no stops, or give
#            a list of stopwords to be used
settings['stopword'] = '0'

# NGRAM: 1 to use bigram, 0 to use unigram
settings['ngram'] = '0'

json.dump(settings, 
          open( 
               os.path.join(
                            'settings',
                            project_name + '_settings.json'), 
               'w'),
          indent=2)

# <codecell>

!cat settings/crp_expenditures_nov4_7-6_settings.json

# <codecell>

tp_option_str = "-stopword {stopword} -stemming {stemming}".format(**settings)
text_processor = TextPreprocessor(option=tp_option_str)

# <codecell>

fg_option_str = "-feature {ngram}".format(**settings)
feature_generator = FeatureGenerator(option=fg_option_str)

# <codecell>

text_converter = Text2svmConverter()

# <codecell>

text_converter.feat_gen = feature_generator
text_converter.text_prep = text_processor

# <codecell>


# <codecell>

convert_text(train_csv, text_converter, train_svm)

# <codecell>

text_converter.save(os.path.join(CONVERTER_DIR, project_name + '.converter'))

# <codecell>

!head data/labeled/train/crp_expenditures_nov4_7-16_train.svm

# <codecell>

!head data/clean/crp_expenditures_nov4_7-16_train.csv

# <codecell>

text_model = train_converted_text(train_svm, text_converter)

# <codecell>

text_model.save(os.path.join(MODEL_DIR,project_name+'.model'))

# <codecell>


