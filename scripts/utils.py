#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil

def generate_data_set(annot_dir, frames_dir, img_dir):

    f = []    

    for (dirpath, dirnames, filenames) in os.walk(annot_dir):
        f.extend(filenames)
        break

    f = [_file for _file in f if _file.endswith(".png")]

    for _file in f:
        file_name = frames_dir + "/" + _file
        destination = img_dir + "/" + _file
        shutil.copyfile(file_name, destination)

    return

if __name__=="__main__":

    annot_dir = "/home/btran/publicWorkspace/data/hsr/annotations/"
    frames_dir = "/home/btran/publicWorkspace/data/hsr/frames/"
    img_dir = "/home/btran/publicWorkspace/data/hsr/imgs/"

    generate_data_set(annot_dir, frames_dir, img_dir)
