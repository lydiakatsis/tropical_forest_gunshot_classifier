# Contents #
This folder contains the scripts used in the paper 'Automated detection of gunshots in tropical forests using convolutional neural networks' https://doi.org/10.1016/j.ecolind.2022.109128

Files include:
* `train_GUNSHOT_classifier round 8.py` contains the script used to train the gunshot classification CNN, including the data augmentation pipeline.
* `Best.model` contains the final, best-performing model that was used in the manuscript. This model only works with OpSo 0.5
* `predict_GUNSHOT_classifier.py` shows how to use the model to classify gunshots in new datasets. Note that this model classifies 4-second .WAV files (see http://opensoundscape.org/en/latest/ for how to predict on longer files) 

Note, this code is based upon Opensoundscape 0.6.0, and are not compatible with latest updates to the library.
