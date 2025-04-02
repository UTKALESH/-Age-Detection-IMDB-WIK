**README.md**

# Fine-Tuned Age Detection Model

## Overview
This project fine-tunes a pre-trained **VGG16** model to perform age detection using the **IMDB-WIKI dataset**. The model extracts features from images and predicts the person's age.

## Dataset
- The dataset is located at `/content/drive/MyDrive/DATASET/IMBD WIKI`.
- The model extracts the birth year and photo year from the filenames to compute the age.

## Installation
To set up the environment, install the required dependencies:
```bash
pip install -r requirements.txt
```

## Training the Model
Run the following command to train the model:
```bash
python train.py
```

## Model Architecture
- **Pre-trained VGG16 (frozen layers)** for feature extraction.
- **Custom layers** (GlobalAveragePooling, Dense, Dropout) for regression.

## Output
- The trained model is saved as `fine_tuned_age_detection_model.h5`.

## Dependencies
See `requirements.txt` for all necessary libraries.

---
