import json
from PIL import Image
import numpy as np
import os
yourpath = './data/men'
upath='./data/women'

json_data = json.load(open('./data/imgs_men.json'))
images=[]
labels=[]
for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:
        im_frame = Image.open(os.path.join(root, name))
        np_frame = np.array(im_frame)
        images.append(np_frame)
        labels.append('0')
print('men over')

for root, dirs, files in os.walk(upath, topdown=False):
    for name in files:
        im_frame = Image.open(os.path.join(root, name))
        np_frame = np.array(im_frame)
        images.append(np_frame)
        labels.append('1')
print('women over')
x=np.array(images)
y=np.array(labels)
print(x.shape)
print(y.shape)
np.savez('training_data.npz', imgs=x, labels=y)

