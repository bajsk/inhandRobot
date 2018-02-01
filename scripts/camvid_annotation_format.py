#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import walk
import argparse
import cv2

def changeToCamVidFormat(img):
    height, width = img.shape[:2]
    for i in range(height):
        for j in range(width):
            red_val = img.item(i, j, 2)
            img[i, j] = [red_val, red_val, red_val]

    return img

def camvid_annotation_format(annotation_path, output_annotation_dir):
    f = []    
    for (dirpath, dirnames, filenames) in walk(annotation_path):
        f.extend(filenames)
        break

    f = [_file for _file in f if _file.endswith(".png")]
    
    for file_name in f:
        file_path = annotation_path + file_name
        output_file_path = output_annotation_dir + file_name
        img = cv2.imread(file_path)
        output_img = changeToCamVidFormat(img)
        cv2.imwrite(output_file_path, output_img)

    return

if __name__=="__main__":

    parser = argparse.ArgumentParser()    
    parser.add_argument("--annotation_dir",
                        type=str,
                        default="/home/btran/publicWorkspace/dev/js-segment-annotator/data/annotations/")
    parser.add_argument("--output_annotation_dir",
                        type=str,
                        default="/home/btran/publicWorkspace/data/hsr/annotations/")
    
    args = parser.parse_args()
    camvid_annotation_format(args.annotation_dir, args.output_annotation_dir)
