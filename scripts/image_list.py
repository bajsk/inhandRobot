#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import os
import shutil
from PIL import Image

def image_list(frames_dir):

    original_frames = []
    for (dirpath, dirnames, filenames) in os.walk(frames_dir):
        original_frames.extend(filenames)
        break
    
    original_frames = [_file[:-4] for _file in original_frames if _file.endswith(".png")]    
    len_original_frames = len(original_frames)

    f = open("train_aug.txt", "w")
    
    for i, original_frame in enumerate(original_frames):
        print original_frame
        f.write(original_frame + "\n")

    f.close()
    
    return

if __name__=="__main__":

    frames_dir = "/home/btran/publicWorkspace/dev/inhandRobot/data/augmented_data/frames/"
    image_list(frames_dir)
