
import os


FLAG = 1
if FLAG == 1:

    ##train
    img_path = "/Users/shaoben/Documents/dataset/DETRAC/train_detrac/images"
    img_dir = os.listdir(img_path) #image
    lb_dir = os.listdir("/Users/shaoben/Documents/dataset/DETRAC/train_detrac/labels")

else:
    ##test
    img_path = "/Users/shaoben/Documents/dataset/DETRAC/val_detrac/images"
    img_dir = os.listdir(img_path) #image
    lb_dir = os.listdir("/Users/shaoben/Documents/dataset/DETRAC/val_detrac/labels")

count=0
for img in img_dir:
    # print(img.split(".")[0]+".txt")

    if img.split(".")[0]+".txt" in lb_dir:
        # print(1)
        pass
    else:
        print(img)
        os.remove(os.path.join(img_path, img))
        count+=1
print(count)


