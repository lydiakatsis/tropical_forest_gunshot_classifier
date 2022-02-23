# Tropical forest gunshot classifier

Reproducability code for "Automated detection of gunshots in tropical forests using convolutional neural networks" (Katsis et. al. 2022, in prep.)

This associated data used for model training and validation (749 gunshots, and 35239 background sounds collected in tropical forest sites in Belize) is archived on [TBD]:

[insert link when available]

All scripts and workflow in this repo are based heavily on OpenSoundscape 0.5.0 http://opensoundscape.org/en/latest/, created by the Kitzes Lab.

Requirements:
Python 3.7
Opensoundscape 0.6.1


## Model training script ##
`train_GUNSHOT_classifier round 8.py` contains the script used to train the gunshot classification CNN, including the data augmentation pipeline.

## Final model ##
`Best.model` contains the final, best-performing model that was used in the manuscript.

## Prediction script ##
`predict_GUNSHOT_classifier.py` shows how to use the model to classify gunshots in new datasets. Note that this model classifies 4-second .WAV files (see http://opensoundscape.org/en/latest/ for how to predict on longer files) 

