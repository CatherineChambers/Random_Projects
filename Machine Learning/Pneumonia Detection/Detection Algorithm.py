import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from tensorflow.keras import datasets, layers, models

train_dir = "../Pneumonia Detection/chest_xray/train"
test_dir = "../Pneumonia Detection/chest_xray/test"
val_dir = "../Pneumonia Detection/chest_xray/val"

print("Train set:")
print("-" * 60)
num_pneumonia = len(os.listdir(os.path.join(train_dir, 'PNEUMONIA')))
num_normal = len(os.listdir(os.path.join(train_dir, 'NORMAL')))
print(f"PNEUMONIA={num_pneumonia}")
print(f"NORMAL={num_normal}")

print("\nTest set:")
print('-' * 60)
print(f"PNEUMONIA={len(os.listdir(os.path.join(test_dir, 'PNEUMONIA')))}")
print(f"NORMAL={len(os.listdir(os.path.join(test_dir, 'NORMAL')))}")

print("\nValidation set")
print('-' * 60)
print(f"PNEUMONIA={len(os.listdir(os.path.join(val_dir, 'PNEUMONIA')))}")
print(f"NORMAL={len(os.listdir(os.path.join(val_dir, 'NORMAL')))}")

pneumonia = os.listdir("../Pneumonia Detection/chest_xray/train/PNEUMONIA")
pneumonia_dir = "../Pneumonia Detection/chest_xray/train/PNEUMONIA/"

# load the image
img = load_img(pneumonia_dir + pneumonia[0])

# show the image
img.show()
# convert to numpy array
img_array = img_to_array(img)

print("type:", img_array.dtype)
print("shape:", img_array.shape)

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

