#!/usr/bin/env python
# coding: utf-8

# # train_GUNSHOT_classifier
# Opso 0.5.0 
# Version date = 02/11/2021
# Retraining model after feedback from Kitzes lab
# 
# Main changes:
# - Instead of first augmentation, just upsampled gunshots
# - batch size = 64
# - no augmentation on validation data
# 
# Round 1: upsample gunshots to match number of background sounds (5000), augmentation, bactch size = 64
# 
# If have time, run models below
# Round 2: upsample gunshots to match number of background sounds, no augmentation
# Round 3: downsample background sounds to match number of gunshots, no augmentation
# 
# 

# In[5]:


# load packages
from opensoundscape.preprocess.preprocessors import BasePreprocessor, AudioToSpectrogramPreprocessor, CnnPreprocessor
from opensoundscape.torch.models.cnn import PytorchModel, Resnet18Multiclass, Resnet18Binary, InceptionV3
from opensoundscape import data_selection


#other utilities and packages
from opensoundscape.helpers import run_command
import torch
import pandas as pd
from pathlib import Path
import numpy as np
import pandas as pd
import random
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
import os
from datetime import date
from glob import glob


#==========Set Paths to Files==========
d = date.today()
d = d.strftime('%y%m%d')
outputs = './Outputs_round_8_/' #Where I want to save the outputs of this script.
os.mkdir(outputs)
model_save = './GUNSHOT_8_'+d+'/' #The location of my saved model.
 ####The location of my training data  For snowy will be /media/kitzeslab/Hardrive name
data ='/media/kitzeslab/star_000/gunshot_cnn/'  
data_dir = '/media/kitzeslab/star_000/gunshot_cnn/'
data = '/media/kitzeslab/star_000/gunshot_cnn/mix_training_set/*/*/' #The location of my training data.
label_data = '/media/kitzeslab/star_000/gunshot_cnn/mix_training_set/' # cd PThe location of the csv of labels


train_path_background = [os.path.normpath(i) for i in glob(label_data +'train/gunshot/*.WAV')]
# downsample background sounds to 5000
#train_background_path = random.sample([os.path.normpath(i) for i in glob(label_data +'train/background/*.WAV')],10000)
train_background_path = [os.path.normpath(i) for i in glob(label_data +'train/background/*.WAV')]
train_path = train_path_background + train_background_path
train_df = pd.DataFrame({'filename':train_path})
train_df['category'] = [os.path.basename(os.path.dirname(i)) for i in train_df['filename']]
train_df['presence'] = [0 if label=='background' else 1 for label in train_df['category']]
train_df = train_df[['filename', 'presence']]
train_df.to_csv(outputs + 'train_labels.csv')

val_path = [os.path.normpath(i) for i in glob(label_data +'val/*/*.WAV')]
val_df = pd.DataFrame({'filename':val_path})
val_df['category'] = [os.path.basename(os.path.dirname(i)) for i in val_df['filename']]
val_df['presence'] = [0 if label=='background' else 1 for label in val_df['category']]
val_df = val_df[['filename', 'presence']]
val_df.to_csv('val_labels.csv')

#==========Labels==========
#load labels
train_labels = train_df
#Load a csv with presence/absence designations to each clip.

#convert labels file into other format
#Here's where you set up your classes and file labels
#train_labels.filename = [data_dir+f for f in train_labels.filename]
train_labels['negative'] = [0 if label==1 else 1 for label in train_labels['presence']]
train_labels['positive'] = [1 if label==1 else 0 for label in train_labels['presence']]
train_labels = train_labels[['filename','negative','positive']]
train_labels = train_labels.set_index('filename')

# upsample the gunshots to equal the number of absent in training data
train_labels_upsampled = data_selection.upsample(train_labels, label_column='negative', random_state=None)
train_labels_upsampled.to_csv(outputs+'labels_used_'+d+'.csv')

#### Val labels
val_labels = val_df 
#Load a csv with presence/absence designations to each clip.

#convert labels file into other format
#Here's where you set up your classes and file labels
#val_labels.filename = [data_dir+f for f in val_labels.filename]
val_labels['negative'] = [0 if label==1 else 1 for label in val_labels['presence']]
val_labels['positive'] = [1 if label==1 else 0 for label in val_labels['presence']]
val_labels = val_labels[['filename','negative','positive']]
val_labels = val_labels.set_index('filename')

val_labels.to_csv(outputs+'val_labels_'+d+'.csv')


# Preprocess audio data
#initialize a preprocessor and provide a dataframe with samples to use as overlays

train_dataset = CnnPreprocessor(train_labels_upsampled, overlay_df=train_labels_upsampled)
train_dataset.augmentation_on()
train_dataset.actions.overlay.set(overlay_class='negative', overlay_weight=0.4)
#train_dataset.actions.add_noise.set(std=0.2)
train_dataset.actions.random_affine.on()
train_dataset.actions.load_audio.set(sample_rate=8000)
train_dataset.actions.frequency_mask.set(max_width = 0.1, max_masks=20)
train_dataset.actions.time_mask.set(max_width = 0.1, max_masks=20)
train_dataset.actions.bandpass.set(min_f=0,max_f=2000)
train_dataset.actions.bandpass.on()
train_dataset.actions.to_spec.set(window_samples=256,overlap_samples=256/2)

# For validation dataset just resample, bandpass, and set spec parameters
val_dataset = AudioToSpectrogramPreprocessor(val_labels)
val_dataset.actions.load_audio.set(sample_rate=8000)
val_dataset.actions.bandpass.set(min_f=0,max_f=2000)
val_dataset.actions.bandpass.on()
val_dataset.actions.to_spec.set(window_samples=256,overlap_samples=256/2)

#==========Create & Train Model==========
classes = train_labels_upsampled.columns

#load the model
#Would probably use Resnet18Multiclass

model = Resnet18Binary(classes)

#train the model
model.train(
    train_dataset=train_dataset,
    valid_dataset=val_dataset,
    save_path=model_save,
    epochs=50,
    batch_size=64,
    save_interval=5,
    num_workers = 4
)


# In[ ]:


# Plot model training metrics to look at overfitting
def metrics(source_text, metric):
    
    results = []
    if 'precision' in metric or 'recall' in metric or 'f1' in metric or "hamming_loss" in metric:
        for key in source_text.keys():
            results.append(source_text[key][metric])
        return[results]


# In[ ]:


fig, ax = plt.subplots(1, 1)

ax.scatter(model.train_metrics.keys(), metrics(model.train_metrics, "hamming_loss"), label = "training")
ax.scatter(model.valid_metrics.keys(), metrics(model.valid_metrics, "hamming_loss"), label = "validation")

ax.set_ylim(0, 1)

plt.xlabel('epoch')
plt.ylabel("loss")
plt.legend()
plt.title("Optimization learning curve")

#plt.show()

plt.savefig(outputs+'loss_'+d+ '.png')


# In[ ]:


fig, ax = plt.subplots(1, 1)

ax.scatter(model.train_metrics.keys(), metrics(model.train_metrics, "f1"), label = "training")
ax.scatter(model.valid_metrics.keys(), metrics(model.valid_metrics, "f1"), label = "validation")

ax.set_ylim(0, 1)

plt.xlabel('epoch')
plt.ylabel(" ")
plt.legend()
plt.title("Performance learning curve")

#plt.show()

plt.savefig(outputs+'f1_'+d+ '.png')


# In[ ]:




