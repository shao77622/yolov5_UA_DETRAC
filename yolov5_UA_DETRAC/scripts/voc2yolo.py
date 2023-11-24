# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
from os import getcwd

# sets = ['train', 'val', 'test']
# sets = ['train_bitvehicle']
classes = ["car"]   # 改成自己的类别
abs_path = os.getcwd()
print(abs_path)

def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h

def convert_annotation(image_id):
    in_file = open('/Users/shaoben/Documents/dataset/BITVehicle/train_bitvehicle/labels/%s.xml' % (image_id), encoding='UTF-8')
    out_file = open('/Users/shaoben/Documents/dataset/BITVehicle/train_bitvehicle/labels_txt/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text.replace("[[", "").replace("]]", ""))
    h = int(size.find('height').text.replace("[[", "").replace("]]", ""))
    for obj in root.iter('object'):
        # difficult = obj.find('difficult').text
        # difficult = obj.find('difficult').text
        # cls = obj.find('name').text
        # if cls not in classes or int(difficult) == 1:
        #     continue
        cls_id = 0
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        b1, b2, b3, b4 = b
        # 标注越界修正
        if b2 > w:
            b2 = w
        if b4 > h:
            b4 = h
        b = (b1, b2, b3, b4)
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    out_file.flush()

wd = getcwd()
# for image_set in sets:
if not os.path.exists('/Users/shaoben/Documents/dataset/BITVehicle/train_bitvehicle/labels_txt'):
    os.makedirs('/Users/shaoben/Documents/dataset/BITVehicle/train_bitvehicle/labels_txt')
label_file_names = os.listdir(
    '/Users/shaoben/Documents/dataset/BITVehicle/train_bitvehicle/labels')
for label_file_name in label_file_names:
    # print(label_file_name.split(".")[0])
    convert_annotation(label_file_name.split(".")[0])
    # break
