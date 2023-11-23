
import os

##train
train_img_path = "/Users/shaoben/Documents/dataset/DETRAC/train_detrac/images"
train_img_dir = os.listdir(train_img_path)  # image
train_lb_path="/Users/shaoben/Documents/dataset/DETRAC/train_detrac/labels"
train_lb_dir = os.listdir(train_lb_path)

##test
val_img_path = "/Users/shaoben/Documents/dataset/DETRAC/val_detrac/images"
val_img_dir = os.listdir(val_img_path)  # image
val_lb_path="/Users/shaoben/Documents/dataset/DETRAC/val_detrac/labels"
val_lb_dir = os.listdir(val_lb_path)

val_count=len(val_img_dir)

val_img_dir = sorted(val_img_dir)
val_lb_dir = sorted(val_lb_dir)

for i in range(val_count):
    if i % 2 ==0:
        cmd = "mv {} {}".format(os.path.join(val_img_path, val_img_dir[i]), train_img_path)
        print(cmd)
        os.system(cmd)
        cmd = "mv {} {}".format(os.path.join(val_lb_path, val_img_dir[i].split(".")[0]+".txt"), train_lb_path)
        print(cmd)
        os.system(cmd)



