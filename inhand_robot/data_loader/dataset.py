#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import sys
import cv2
import numpy as np
import torch.utils.data as data
from .data_loader_base import BaseDataset


_CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
try:
    sys.path.append(os.path.join(_CURRENT_DIR, ".."))
    from utility.visualization import generate_color_chart
except:
    print("Cannot load utility")
    exit(0)


class HSRInhandObjectsDataset(BaseDataset):
    def __init__(self, images_file_path, labels_file_path, classes, phase="train", transform=None, train_val_ratio=0.8):
        super(HSRInhandObjectsDataset, self).__init__(images_file_path, labels_file_path, classes, phase, transform)

        self._all_images_path = np.array([line.rstrip("\n") for line in open(images_file_path)])
        self._all_labels_path = np.array([line.rstrip("\n") for line in open(labels_file_path)])

        if len(self._all_images_path) == 0 or len(self._all_labels_path) == 0:
            raise Exception("No samples parsed")

        self._colors = generate_color_chart(num_classes=len(self._classes))
        self._legend = BaseDataset.show_color_chart(self.classes, self._colors)
        self._phase = phase

        np.random.seed(1590)
        num_all_images = len(self._all_images_path)
        num_train = int(0.8 * num_all_images)
        train_idx = np.random.choice(range(num_all_images), num_train)
        test_idx = np.array([i for i in range(num_all_images) if i not in train_idx])

        if self._phase == "train":
            self._image_paths = self._all_images_path[train_idx]
            self._gt_paths = self._all_labels_path[train_idx]
        else:
            self._image_paths = self._all_images_path[test_idx]
            self._gt_paths = self._all_labels_path[test_idx]

    @property
    def legend(self):
        return self._legend

    @property
    def image_paths(self):
        return self._image_paths

    @property
    def gt_paths(self):
        return self._gt_paths
