#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

directory_root = os.path.dirname(os.path.realpath(__file__)) + "/../"
data_path = directory_root + "/data/augmented_data/"
model_path = directory_root + "/models/"
log_path = directory_root + "/logs/"

class Config():

    data_dir = data_path
    model_dir = model_path
    log_dir = log_path

    preprocess = None
