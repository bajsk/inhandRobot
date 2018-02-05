#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import torch
import torchvision
from torch.utils.data import DataLoader, Dataset
from PIL import Image

from config import Config

class InhandDataset(Dataset):

    def __init__(self, data_path = Config.data_dir, preprocess = Config.preprocess):
        
