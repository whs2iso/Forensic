# -*- coding: utf-8 -*-
"""DFC2023-104-1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QKYjDfNPCI0cCp-8XgAowiAuAPbcU2Rx
"""

from google.colab import drive
import matplotlib.pyplot as plt
import numpy as np
import librosa

drive.mount('/content/gdrive')

original_audio, sr_original_audio = librosa.load('/content/gdrive/MyDrive/original.wav')
modified_mix_audio, sr_modified_mix_audio = librosa.load('/content/gdrive/MyDrive/modified.wav')

A_original_audio = np.abs(librosa.stft(original_audio))
A_modified_mix_audio = np.abs(librosa.stft(modified_mix_audio))

threshold = 1
time_frame = np.sum(np.abs(A_original_audio - A_modified_mix_audio), axis =0)

plt.plot(time_frame)
plt.title('Time Frame Difference')
plt.xlabel('Time Frame')
plt.ylabel('Difference')
plt.show()

# 임계값을 넘는 인덱스 찾기
indices_where_exceeds_threshold = np.where(time_frame > threshold)[0]

# 변경된 음성이 시작되는 인덱스 찾기
modified_voice_start = indices_where_exceeds_threshold[0] if indices_where_exceeds_threshold.size > 0 else None

# 최대값 및 평균값을 분석하여 적절한 임계값을 threshold 변수에 지정
print(f'Difference modified voice start index: {time_frame[modified_voice_start]}')
print(f'Maximum difference until modified voice start index: {np.max(time_frame[:modified_voice_start])}')
print(f'Average difference until modified voice start index: {np.average(time_frame[:modified_voice_start])}')