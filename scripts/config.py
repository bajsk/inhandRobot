#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

directory_root = os.path.dirname(os.path.realpath(__file__)) + "/../"
data_path = directory_root + "/data/augmented_data/"

class Config():

    root_dir = directory_root
    image_path = os.path.join(directory_root, "images")
    data_path = os.path.join(directory_root, "data/augmented_data")
    model_path = os.path.join(directory_root, "models")
    log_dir = os.path.join(directory_root, "logs")
    
    preprocess = None
    model_name = "inhand_robot"
    class_num = 3
