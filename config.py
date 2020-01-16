#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os


_CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class Config(object):
    def __init__(self):
        self.CURRENT_DIR = _CURRENT_DIR

        self.DATA_PATH = os.path.abspath(os.path.join(_CURRENT_DIR, "data"))

        self.IMAGES_FILE_PATH = os.path.join(self.DATA_PATH, "all_train_list.txt")

        self.LABELS_FILE_PATH = os.path.join(self.DATA_PATH, "all_label_list.txt")

        self.CLASSES = ["background", "robot_hand", "inhand_obj"]

        self.NUM_CLASSES = len(self.CLASSES)

        self.CLASS_IDX_TO_NAME = {0: "background", 1: "robot_hand", 2: "inhand_obj"}

        self.CLASS_NAME_TO_IDX = {"background": 0, "robot_hand": 1, "inhand_obj": 2}

    def display(self):
        """
        Display Configuration values.
        """
        print("\nConfigurations:")
        for a in dir(self):
            if not a.startswith("__") and not callable(getattr(self, a)):
                print("{:30} {}".format(a, getattr(self, a)))
                print("\n")
