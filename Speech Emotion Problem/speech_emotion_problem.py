# -*- coding: utf-8 -*-
"""speech-emotion-problem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qOMAQiNV0QUEvzXk4RVtuFOjUYBiZ-5V
"""

!pip install librosa soundfile sklearn 


import librosa
import librosa.display
import soundfile
import numpy as np 
import pandas as pd
import os
from sklearn.neural_network import MLPClassifier
import pickle 


def extract_feature2(file_name, mfcc, chroma, mel):
  x , sr = librosa.load(audio_path)
  if chroma:
    X = librosa.stft(x)
    result=np.array([])
  if mfcc:
    mfccs = np.mean(librosa.feature.mfcc(y=x, sr=sr))
    result=np.hstack((result, mfccs))
  if chroma:
    chroma=np.mean(librosa.feature.chroma_stft(S=X, sr=sr).T,axis=0)
    result=np.hstack((result, chroma))
  if mel:
    mel = np.mean(librosa.feature.melspectrogram(x, sr=sr).T,axis=0)
    result=np.hstack((result, mel))
  return result

path = ''

x_test = []
files = []
model = pickle.load(dbfile)

for file in os.listdir(path):
    file_name = os.path.basename(file)
    feature = extract_feature2(file_name, mfcc=True, chroma=True, mel=True)
    x_test.append(feature)
    files.append(file_name)

y_pred = model.predict(x_test)

submission = pd.DataFrame({
        "file_name": files,
        "emotion": y_pred
    })

submission.to_csv('submission.csv', index=False)

submission = pd.read_csv('submission.csv')
submission.head()