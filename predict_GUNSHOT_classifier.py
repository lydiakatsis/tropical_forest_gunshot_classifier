#!/usr/bin/env python
# coding: utf-8

# # Full predictions GUNSHOTS

#==========Import Utilities==========
from opensoundscape.preprocess.preprocessors import AudioToSpectrogramPreprocessor
from opensoundscape.torch.models.cnn import Resnet18Binary
from opensoundscape.helpers import run_command

# Other utilities and packages
import torch
from pathlib import Path
import numpy as np
import pandas as pd
from glob import glob
import os
import time
from datetime import date


#==========Set Paths to Files==========
modeldate = '211111'
model_location = './GUNSHOT_8_'+modeldate+'/'
d = date.today()
d = d.strftime('%y%m%d')
o = "./Outputs_predictions" + d + "/"
os.mkdir(o)
i = "/media/kitzeslab/star_000/gunshot_cnn/bnr_all_test"  # Path to where all the prediction data is stored on hardrive

#==========Load Model==========
model = Resnet18Binary(classes=['negative','positive'])
model.load(model_location + 'best.model')


#==========Preprocess Audio==========
file_list = glob(i+'/*.WAV')   # make sure this sends us to where data is
#file_list = file_list[:1000] #comment out if not testing
audio_file_df = pd.DataFrame(index=file_list)
batch_size = int((len(file_list)/10)+0.5)
batches = [(i*batch_size,(i+1)*batch_size) if i < 9 else (i*batch_size,len(file_list)) for i in range(10)]
full_scores = pd.DataFrame()
full_preds = pd.DataFrame()

for i in range(len(batches)):
    t1 = int(time.time())
    df = audio_file_df[batches[i][0]:batches[i][1]]
    prediction_dataset = AudioToSpectrogramPreprocessor(df, return_labels=False)
    prediction_dataset.actions.load_audio.set(sample_rate=8000)
    prediction_dataset.actions.bandpass.set(min_f=0,max_f=2000)
    prediction_dataset.actions.bandpass.on()
    prediction_dataset.actions.to_spec.set(window_samples=256,overlap_samples=256/2)

#==========Generate Predictions==========
    scores, preds, labels = model.predict(
                    prediction_dataset,
                    batch_size=64,
                    num_workers=4,
                    activation_layer="softmax",
                    binary_preds='multi_target',
                    threshold= 0.808802
                )

    full_scores = pd.concat([full_scores,scores])
    full_preds = pd.concat([full_preds,preds])

full_scores.sort_values(by=['positive'], ascending=False, inplace=True)

full_scores.to_csv(o+"GUNSHOT_scores.csv")
full_preds.to_csv(o+"GUNSHOT_binary_predictions.csv")

