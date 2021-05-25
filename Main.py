from MFCC import MFCC
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Settings
model_path = "wake_word.model"
wav_path   = "Testdata/stop/11.wav"

# Extract the features
mf = MFCC()

# Load Model
model = keras.models.load_model(model_path)

# Extract Feature
extracted = mf.extractFeatures(wav_path)

# Normalisasi
finalReshape = extracted.reshape(extracted.shape[0], extracted.shape[1], 1)
finalReshape = np.expand_dims(finalReshape, 0)
sample = [finalReshape]

# Predicting
predictions = model.predict(sample)
predictions = predictions[0][0]
print("Prediction : ", predictions)
