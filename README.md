**README.md**

# Age Detection Model (IMDB-WIKI Dataset)

## Overview
This project implements a **CNN-based age detection model** using the **IMDB-WIKI dataset**. The model processes images of faces and predicts the estimated age based on facial features.

## Dataset
- The dataset is located at `/content/drive/MyDrive/DATASET/IMBD WIKI`.
- The model extracts birth year and photo year from filenames to calculate the age.

## Installation
To set up the environment, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Training the Model
Run the following command to train the model:

```bash
python imbd_wiki.py
```

## Model Architecture
- **CNN Model with the following layers:**
  - Conv2D layers with ReLU activation
  - MaxPooling layers
  - Flatten layer
  - Dense layers with Dropout for regularization
- **Mean Squared Error (MSE) loss function** for regression.
- **Adam optimizer** with a learning rate of `0.001`.

## Output
- The trained model is saved as `age_detection_model.h5`.

## Dependencies
See `requirements.txt` for all necessary libraries.

---
