#!/bin/bash

SRC_DIR="/home/blannon/src/libshorttext-1.0"

EXP_DIR="/home/blannon/experiments/CRP-expenditures_learn-type-codes"
DATA_DIR="$EXP_DIR/data"
CLEAN_DIR="$DATA_DIR/clean"
TRAIN_DIR="$DATA_DIR/labeled/train"
#TEST_DIR="$DATA_DIR/labeled/test"
#UNLABELED_DIR="$DATA_DIR/unlabeled"
CONVERTER_DIR="$EXP_DIR/converters"

DIMENSION="descrip"
TRANSFORMATION="labeled"

ORIG="$CLEAN_DIR/$DIMENSION.$TRANSFORMATION.csv"
#TRAIN="$TRAIN_DIR/$DIMENSION.$TRANSFORMATION.csv"
#TEST="$TEST_DIR/$DIMENSION.$TRANSFORMATION.csv"
#UNLABELED="$UNLABELED_DIR/$DIMENSION.$TRANSFORMATION.csv"

echo `wc -l $ORIG`

time python $SRC_DIR/text2svm.py -P 2 $ORIG

TMP_CONVERT="$ORIG.text_converter"
TMP_SVM="$ORIG.svm"

mv $TMP_CONVERT $CONVERTER_DIR/
mv $TMP_SVM $TRAIN_DIR/
