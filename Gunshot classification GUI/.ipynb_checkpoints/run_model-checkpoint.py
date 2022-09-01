#!/usr/bin/env python
# coding: utf-8

# # Full predictions GUNSHOTS

#==========Import Utilities==========
from opensoundscape.torch.models.cnn import load_outdated_model
from opensoundscape.torch.models.cnn import load_model
from opensoundscape.audio import Audio
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

start_time = time.time()

cpus = psutil.cpu_count()

#==========Load Model==========
url = 'https://www.dropbox.com/s/qnno1u648fa8ovd/outdated_model.model?dl=0'

subprocess.run(['curl',
                url,
                '-L', '-o', './model1.model', '--no-verbose'])

model = load_model('model1.model')


#=========Preprocess Audio==========
file_list = glob('*.WAV') + glob('*.wav')
file_length = Audio.from_file(file_list[1]).duration()
no_files = len(file_list)

audio_file_df = pd.DataFrame(index=file_list)
full_scores = pd.DataFrame()
full_preds = pd.DataFrame()

if file_length > 14400:
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

elif int(no_files) < 30:
    for i in range(int(file_length)):
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
    
else:   
    batch_size = int((len(file_list)/10)+0.5)    
    batches = [(i*batch_size,(i+1)*batch_size) if i < 9 else (i*batch_size,len(file_list)) for i in range(10)]

    for i in range(len(batches)):
        t1 = int(time.time())
        print("Classifying batch  " + str(i+1) + " of " + str(len(batches)) +'...')   
        df = audio_file_df[batches[i][0]:batches[i][1]]
        
        #==========Generate Predictions==========
        scores, preds, unsafe = model.predict(
                        df,
                        batch_size=64,
                        num_workers=cpus,
                        activation_layer="softmax",
                        binary_preds='single_target'
                    )
    
    
        t2 = int(time.time())
        print("Finished classifying batch " +  str(i+1) + ' in ' + str(int(t2 - t1)) + ' seconds!\n')
        
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