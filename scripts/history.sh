#!/bin/bash

EXP_DIR="/home/blannon/experiments/CRP-expenditures_learn-type-codes"
DATA_DIR="$EXP_DIR/data"
CLEAN_DIR="$DATA_DIR/clean"
TRAIN_DIR="$DATA_DIR/labeled/train"
TEST_DIR="$DATA_DIR/labeled/test"
UNLABELED_DIR="$DATA_DIR/unlabeled"

DIMENSION="description"

ALL="$CLEAN_DIR/expends2012.all.$DIMENSION.csv"
TRAIN="$TRAIN_DIR/expends2012.$DIMENSION.sorted-labeled.csv"
TEST="$TEST_DIR/expends2012.$DIMENSION.sorted-labeled-uniq.csv"
UNLABELED="$UNLABELED_DIR/expends2012.$DIMENSION.unlabeled.csv"

grep -v -P "^\?" $ALL | sort > $TRAIN
grep -v -P "^\?" $ALL | sort | uniq > $TEST
grep -P "^\?" $ALL | sort | uniq > $UNLABELED
