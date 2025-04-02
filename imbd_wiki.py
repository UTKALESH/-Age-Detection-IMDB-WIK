# -*- coding: utf-8 -*-
"""IMBD-WIKI

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16YubA7oHNon1bYtDo11YBz_-blTYdepw
"""

import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split

# Set dataset path
data_path = "/content/drive/MyDrive/DATASET/IMBD WIKI"

def extract_age_from_filename(filename):
    try:
        parts = filename.split("_")
        birth_year = int(parts[2].split("-")[0])  # Extract birth year
        photo_year = int(parts[3].split(".")[0])  # Extract photo year
        return photo_year - birth_year  # Compute age
    except:
        return None

def load_data(data_path, img_size=(128, 128)):
    images = []
    ages = []
    for filename in os.listdir(data_path):
        img_path = os.path.join(data_path, filename)
        if filename.endswith(".jpg"):
            age = extract_age_from_filename(filename)
            if age is not None:
                try:
                    img = cv2.imread(img_path)
                    img = cv2.resize(img, img_size)
                    img = img / 255.0  # Normalize
                    images.append(img)
                    ages.append(age)
                except:
                    continue
    return np.array(images), np.array(ages)

# Load images and labels
X, y = load_data(data_path)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(1)  # Regression output
])

# Compile model
model.compile(optimizer=Adam(learning_rate=0.001), loss='mse', metrics=['mae'])

# Train model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=32)

# Save model
model.save("age_detection_model.h5")

print("Model training complete and saved.")

