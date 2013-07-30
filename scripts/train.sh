#!/bin/bash

LST_DIR="/home/blannon/src/libshorttext-1.0"

EXP_DIR="/home/blannon/experiments/CRP-expenditures_learn-type-codes"

DATA_DIR="$EXP_DIR/data"
CLEAN_DIR="$DATA_DIR/clean"
TRAIN_DIR="$DATA_DIR/labeled/train"
TEST_DIR="$DATA_DIR/labeled/test"
UNLABELED_DIR="$DATA_DIR/unlabeled"

CONVERTER_DIR="$EXP_DIR/converters"

MODEL_DIR="$EXP_DIR/models"

DIMENSION="descrip"
TRANSFORMATION="labeled"

ALL="$CLEAN_DIR/$DIMENSION.$TRANSFORMATION.csv"
TRAIN_SVM="$TRAIN_DIR/$DIMENSION.$TRANSFORMATION.csv.svm"
CONVERTER="$CONVERTER_DIR/$DIMENSION.$TRANSFORMATION.csv.text_converter"

MODEL="$MODEL_DIR/$DIMENSION.$TRANSFORMATION.csv.svm.model"

python $LST_DIR/text-train.py -P $CONVERTER -f $TRAIN_SVM $MODEL
