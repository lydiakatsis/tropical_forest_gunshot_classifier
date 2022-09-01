#!/usr/bin/env python
# coding: utf-8

# # Full predictions GUNSHOTS

#==========Import Utilities==========
from opensoundscape.torch.models.cnn import load_outdated_model
from opensoundscape.torch.models.cnn import load_model
import opensoundscape

# Other utilities and packages
import torch
from pathlib import Path
import numpy as np
import pandas as pd
from glob import glob
import subprocess
import time
import os
from datetime import date
from tqdm.notebook import tqdm_notebook
import psutil
import sys


start_time = time.time()


# As CPU implementation in opso currently isn't working, this step uses num workers = 0 if on windows computer, otherwise counts the number of CPUs and utilises all
if sys.platform.startswith('win'):
    cpus = 0
else:
    cpus = psutil.cpu_count()

#==========Load Model==========
url = 'https://www.dropbox.com/s/qnno1u648fa8ovd/outdated_model.model?dl=0'

subprocess.run(['curl',
                url,
                '-L', '-o', './model1.model', '--no-verbose'])

model = load_model('model1.model')

#=========Preprocess Audio==========
file_list = glob('*.WAV') + glob('*.wav')
audio_file_df = pd.DataFrame(index=file_list)


file_length = len(file_list)

full_scores = pd.DataFrame()
full_preds = pd.DataFrame()

for i in range(file_length):
    #time.sleep(0.05)
    t1 = int(time.time())
    print("Classifying file  " + str(i+1) + " of " + str(file_length) +'...')    
    
    df = audio_file_df[i:i +1]

#==========Generate Predictions==========
    scores, preds, unsafe = model.predict(
                    df,
                    batch_size=64,
                    num_workers=cpus,
                    activation_layer="softmax",
                    binary_preds='single_target'
                )


    t2 = int(time.time())
    print("Finished classifying file " +  str(i+1) + ' in ' + str(int(t2 - t1)) + ' seconds!\n')
    
    full_scores = pd.concat([full_scores,scores])
    full_scores['folder_name'] = os.path.basename(os.getcwd())

full_scores.sort_values(by=['positive'], ascending=False, inplace=True)
full_scores.to_csv("GUNSHOT_scores.csv")

end_time = time.time()


print("Finished classifying all files in  " + str(int((end_time - start_time)/60)) + ' minutes!\n\n')

print('You should now be able to inspect your results in the csv file saved to this folder called GUNSHOT_scores.csv.\n\nOpen the next program, Results_validation to inspect your results. ' )  

files = ['model1.model', 'run_model.py', 'run_model_1CPU.py']
for d in files:
    try:
        os.remove(d)
    except:
        pass