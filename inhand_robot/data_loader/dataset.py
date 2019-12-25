#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import cv2
import sys
import torch.utils.data as data


_CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
try:
    sys.path.append(os.path.join(_CURRENT_DIR, ".."))
    from utility.visualization import generate_color_chart, show_color_chart
except:
    print("Cannot load utility")
    exit(0)


class HSRInhandObjectsDataLoader(data.Dataset):
    def __init__(self, images_file_path, labels_file_path, classes):
        super(HSRInhandObjectsDataLoader, self).__init__()

        assert(os.path.isfile(images_file_path))
        assert(os.path.isfile(labels_file_path))

        self.__images_path = [line.rstrip("\n") for line in open(images_file_path)]
        self.__labels_path = [line.rstrip("\n") for line in open(labels_file_path)]

        if len(self.__images_path) == 0 or len(self.__labels_path) == 0:
            raise Exception("No samples parsed")

        self.__classes = classes
        self.__colors = generate_color_chart(num_classes=len(self.classes))
        self.__legend = show_color_chart(self.classes, self.__colors)

    @property
    def colors(self):
        return self.__colors

    @property
    def legend(self):
        return self.__legend

    @property
    def classes(self):
        return self.__classes

    def __getitem__(self, idx):
        image_path = self.__images_path[idx]
        label_path = self.__labels_path[idx]

        image = cv2.imread(image_path)
        label = cv2.imread(label_path, 0)

        return image, label

    def get_overlay_image(self, idx):
        image, label = self.__getitem__(idx)
        mask = self.__colors[label]
        overlay = ((0.3 * image) + (0.7 * mask)).astype("uint8")

        return overlay

    def __len__(self):
        return len(self.__images_path)
