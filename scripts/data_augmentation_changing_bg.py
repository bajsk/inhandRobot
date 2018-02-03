#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import os
import shutil
from PIL import Image
import torchvision.transforms as transforms

_preprocess = transforms.Compose([
    transforms.ColorJitter(brightness = 0.1, contrast = 0.1, hue = 0.01)
])

def create_new_img(annot_img, img, bg_img):

    ret, thresh1 = cv2.threshold(annot_img, 0, 255, cv2.THRESH_BINARY)
    thresh1_inv = cv2.bitwise_not(thresh1)

    img_fg = cv2.bitwise_and(img, img, mask = thresh1)
    background_bg = cv2.bitwise_and(bg_img, bg_img, mask = thresh1_inv)

    dst = cv2.add(background_bg, img_fg)
    
    return dst
    
def data_augmentation_changing_bg(annot_dir, frames_dir, bg_dir, result_annot_dir, result_frames_dir):

    original_frames = []
    for (dirpath, dirnames, filenames) in os.walk(annot_dir):
        original_frames.extend(filenames)
        break
    
    original_frames = [_file for _file in original_frames if _file.endswith(".png")]    
    len_original_frames = len(original_frames)
    
    bg_frames = []
    for (dirpath, dirnames, filenames) in os.walk(bg_dir):
        bg_frames.extend(filenames)
        break

    current_frame = 0
    for i, bg_frame in enumerate(bg_frames):

        current_img_name = original_frames[current_frame]
        print current_img_name
        annot_img = cv2.imread(annot_dir + "/" + current_img_name, 0)
        img = cv2.imread(frames_dir + "/" + current_img_name)
        bg_img = cv2.imread(bg_dir + "/" + bg_frame)
        
        dst = create_new_img(annot_img, img, bg_img)
        pil_dst = Image.fromarray(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
        dst = _preprocess(pil_dst)
        
        img_to_copy_name = "augmented_img_" + str(i) + ".png"
        shutil.copyfile(annot_dir + "/" + current_img_name, result_annot_dir + "/" + img_to_copy_name)
        dst.save(result_frames_dir + "/" + img_to_copy_name)
        
        current_frame += 1
        if (current_frame == len_original_frames):
            current_frame = 0

    return

if __name__=="__main__":

    annot_dir = "/home/btran/publicWorkspace/data/hsr/annotations/"
    frames_dir = "/home/btran/publicWorkspace/data/hsr/frames/"
    bg_dir = "/home/btran/publicWorkspace/data/hsr/background2/"
    result_annot_dir = "/home/btran/publicWorkspace/data/hsr/augmented_data/annotations/"
    result_frames_dir = "/home/btran/publicWorkspace/data/hsr/augmented_data/frames/"
    data_augmentation_changing_bg(annot_dir, frames_dir, bg_dir, result_annot_dir, result_frames_dir)
