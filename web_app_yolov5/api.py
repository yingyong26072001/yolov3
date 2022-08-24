import torch
import cv2
import numpy as np
import glob

def Vid2Img(vid_path):
    images = []
    vidcap = cv2.VideoCapture(vid_path)
    count = 0
    success = True
    print(vid_path)
    while success:
      # cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        if not success:
            break
        images.append(image)
        count += 1
    print(count)
    return images

def Img2Vid(images):
    height, width, layers = images[-1].shape

    out = cv2.VideoWriter('processed_output.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))
     
    for i in range(len(images)):
        out.write(images[i])
    out.release()

# vid_path = './shibainu.mp4'
# images = vid2img(vid_path)
# img2vid(images)
