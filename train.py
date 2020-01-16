#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import math
from torch.utils.data import DataLoader
import torch.optim as optim
import torch
from config import Config
from inhand_robot import HSRInhandObjectsDataset, HSRInhandObjectsDataTransform
from torchsummary import summary
import time


def train_model(net, data_loaders_dict, criterion, optimizer, num_epochs, scheduler=None):
    pass

def main():
    pass


if __name__ == '__main__':
    main()
