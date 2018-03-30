#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


import numpy as np

import torch
from torch.autograd import Variable
import torch.nn.functional as F
import deeplab_resnet 
import torch.nn as nn

import cv2
from config import Config

max_label = Config.class_num
gpu0 = 0
model = deeplab_resnet.Res_Deeplab(max_label)
model.eval()
counter = 0
model.cuda(gpu0)

saved_state_dict = torch.load(os.path.join(Config.model_path , Config.model_name + "_20000.pth"))
model.load_state_dict(saved_state_dict)

classes = np.array(('background',
                    'robot_hand', 'inhand_object'))

colormap = [(0,0,0),(0.5,0,0),(0,0.5,0)] + [(0,0,0)] * (256 - len(classes))
colormap = [colormap]
colormap = np.array(colormap) * 255
colormap = colormap.astype(np.uint8)

img = np.zeros((640,640,3))
img_temp = cv2.imread(os.path.join(Config.image_path, "inhand.png")).astype(float)
img_original = img_temp
img_temp[:,:,0] = img_temp[:,:,0] - 104.008
img_temp[:,:,1] = img_temp[:,:,1] - 116.669
img_temp[:,:,2] = img_temp[:,:,2] - 122.675
img[:img_temp.shape[0],:img_temp.shape[1],:] = img_temp
output = model(Variable(torch.from_numpy(img[np.newaxis, :].transpose(0,3,1,2)).float(),volatile = True).cuda(gpu0))
interp = nn.UpsamplingBilinear2d(size=(640, 640))
output = interp(output[3]).cpu().data[0].numpy()
output = output[:,:img_temp.shape[0],:img_temp.shape[1]]

output = output.transpose(1,2,0)
output = np.argmax(output,axis = 2)

output = output.astype(np.int8)
output = cv2.merge((output, output, output))

output_rgb = np.zeros(output.shape, dtype=np.uint8)

cv2.LUT(output, colormap, output_rgb)
cv2.imwrite(os.path.join(Config.image_path, "prediction.png"), output_rgb)        
# cv2.imshow("prediction", output_rgb)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
