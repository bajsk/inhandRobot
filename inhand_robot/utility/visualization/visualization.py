#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2


def generate_color_chart(num_classes=3, seed=100):

    np.random.seed(seed)

    COLORS = np.random.randint(0, 255, size=(num_classes - 1, 3), dtype="uint8")
    COLORS = np.vstack([[0, 0, 0], COLORS]).astype("uint8")

    return COLORS


def show_color_chart(classes, colors):
    legend = np.zeros(((len(classes) * 25) + 25, 300, 3), dtype="uint8")
    for (i, (class_name, color)) in enumerate(zip(classes, colors)):
        color = [int(c) for c in color]
        cv2.putText(legend, class_name, (5, (i * 25) + 17), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.rectangle(legend, (100, (i * 25)), (300, (i * 25) + 25), tuple(color), -1)

    return legend
