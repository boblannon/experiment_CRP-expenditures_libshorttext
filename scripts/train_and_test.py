import sys
import os
import csv
import json

import numpy as np
import pandas as pd

from libshorttext.converter import Text2svmConverter, FeatureGenerator, TextPreprocessor, convert_text
from libshorttext.classifier import train_converted_text

import local_settings as ls

project_name = ls.project_name
BASE_DIR = ls.BASE_DIR


DATA_DIR = os.path.join(BASE_DIR, 'data')
CLEAN_DIR = os.path.join(DATA_DIR, 'clean')
TRAIN_DIR = os.path.join(DATA_DIR, 'labeled', 'train')
TEST_DIR = os.path.join(DATA_DIR, 'labeled', 'test')
CONVERTER_DIR = os.path.join(BASE_DIR, 'converters')
MODEL_DIR = os.path.join(BASE_DIR, 'models')
RESULT_DIR = os.path.join(BASE_DIR, 'results')
OPTIONS_DIR = os.path.join(BASE_DIR, 'options')

train_csv = os.path.join(CLEAN_DIR, project_name + '_train.csv')
test_csv = os.path.join(CLEAN_DIR, project_name + '_test.csv')

train_svm = os.path.join(TRAIN_DIR, project_name + '_train.svm')
test_svm = os.path.join(TEST_DIR, project_name + '_test.svm')

options_json = os.path.join(OPTIONS_DIR, project_name + '_options.json')
        
converter_path = os.path.join(CONVERTER_DIR, project_name + '.converter')

model_path = os.path.join(MODEL_DIR, project_name+'.model')

result_path = os.path.join(RESULT_DIR, project_name+'.result')

def make_dirs(dirlist):
    for d in dirlist:
        if not os.path.exists(d):
            os.makedirs(d)

def make_options():
    options = {}

    # STEMMING: 1 to use porter, 0 for no stemming, or give your 
    #           own stemmer that maps from a list of tokens to a 
    #           list of stemmed tokens
    options['stemming'] = ls.stemming

    # STOPWORDS: 1 to use default stops, 0 for no stops, or give
    #            a list of stopwords to be used
    options['stopword'] = ls.stopword

    # NGRAM: 1 to use bigram, 0 to use unigram
    options['ngram'] = ls.ngram

    json.dump(options, open(options_json, 'w'), indent=2)
    return options

make_dirs([DATA_DIR, CLEAN_DIR, TRAIN_DIR, TEST_DIR, MODEL_DIR, RESULT_DIR, 
            OPTIONS_DIR, CONVERTER_DIR])

options = make_options()

if not os.path.exists(converter_path):
    # Make text processor
    tp_option_str = "-stopword {stopword} -stemming {stemming}".format(**options)
    text_processor = TextPreprocessor(option=tp_option_str)

    # Make feature generator
    fg_option_str = "-feature {ngram}".format(**options)
    feature_generator = FeatureGenerator(option=fg_option_str)

    # Make converter
    text_converter = Text2svmConverter()
    text_converter.feat_gen = feature_generator
    text_converter.text_prep = text_processor

    # Convert Text
    convert_text(train_csv, text_converter, train_svm)

    # Save Converter
    text_converter.save(converter_path)
else:
    text_converter = Text2svmConverter()
    text_converter.load(converter_path)

if not os.path.exists(model_path):
    text_model = train_converted_text(train_svm, text_converter)
    text_model.save(model_path)
else:
    text_model = TextModel(model_path)

prediction_result = predict_text(test_csv, text_model)
prediction_result.save(result_path, analyzable=True)

sys.stderr.write('prediction accuracy was {}\n'.format(
                  prediction_result.get_accuracy()))
sys.stderr.write('prediction results analyzable in {}\n'.format(result_path))
