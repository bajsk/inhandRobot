#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import cv2
import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def bag_to_images(input_dir, output_dir, bag_file, image_topic, downsample):

    bag_file_path = input_dir + bag_file + ".bag"
    print bag_file_path
    bag = rosbag.Bag(input_dir + bag_file + ".bag", "r")
    bridge = CvBridge()
    count = 0
    img_num = 0

    for topic, msg, t in bag.read_messages(topics=[image_topic]):
        if count % downsample == 0:
            cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
            cv2.imwrite(os.path.join(output_dir, bag_file +"_frame%06i.png" % img_num), cv_img)
            print "Wrote image %i" % img_num
            img_num += 1
            
        count += 1

    bag.close()
    return

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("--input_dir",
                        help="Output directory.",
                        type=str,
                        default="/home/btran/publicWorkspace/data/hsr/rosbag/")
    parser.add_argument("--output_dir",
                        help="Output directory.",
                        type=str,
                        default="/home/btran/publicWorkspace/data/hsr/frames/")    
    parser.add_argument("--bag_file",
                        help="Input ROS bag.",
                        type=str,
                        default="2017-11-24-22-34-08")
    parser.add_argument("--image_topic",
                        help="Image topic.",
                        type=str,
                        default="/hsrb/head_rgbd_sensor/rgb/image_rect_color")
    
    parser.add_argument("--downsample",
                        type=int,
                        default=7)

    args = parser.parse_args()

    bag_file_list = ["2017-11-24-22-34-08",
                     "2017-11-24-22-37-05",
                     "2017-11-24-22-40-00",
                     "2017-11-24-22-43-08",
                     "2017-11-24-22-45-53",
                     "2017-11-24-22-49-02",
                     "2017-11-24-22-35-13",
                     "2017-11-24-22-37-47",
                     "2017-11-24-22-41-00",
                     "2017-11-24-22-44-15",
                     "2017-11-24-22-46-38",
                     "2017-11-24-22-50-29",
                     "2017-11-24-22-36-23",
                     "2017-11-24-22-38-39",
                     "2017-11-24-22-42-05",
                     "2017-11-24-22-45-00",
                     "2017-11-24-22-47-50",
                     "2017-11-24-22-51-38"]
    for bag_file in bag_file_list:
        bag_to_images(args.input_dir, args.output_dir, bag_file, args.image_topic, args.downsample)
