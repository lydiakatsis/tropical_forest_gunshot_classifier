# Tropical forest gunshot classifier

Reproducability code for Katsis, L. K. D., et al. (2022). "Automated detection of gunshots in tropical forests using convolutional neural networks." Ecological Indicators 141: 109128.  https://www.sciencedirect.com/science/article/pii/S1470160X22006008 

This associated data used for model training and validation (749 gunshots, and 35239 background sounds collected in tropical forest sites in Belize) is archived on Mendeley Data doi: 10.17632/x48cwz364j.2 https://data.mendeley.com/datasets/x48cwz364j/2

All scripts and workflow in this repo are based heavily on OpenSoundscape 0.5.0 http://opensoundscape.org/en/latest/, created by the Kitzes Lab at the University of Pittsburgh.

Requirements:
- Python 3.7
- Opensoundscape 0.5.0


## Model training script ##
`train_GUNSHOT_classifier round 8.py` contains the script used to train the gunshot classification CNN, including the data augmentation pipeline.

## Final model ##
`Best.model` contains the final, best-performing model that was used in the manuscript. This model only works with OpSo 0.5

'Updated_gunshot_model.model' contains the final model that has been updated to load into OpSo 0.7

## Prediction script ##
`predict_GUNSHOT_classifier.py` shows how to use the model to classify gunshots in new datasets. Note that this model classifies 4-second .WAV files (see http://opensoundscape.org/en/latest/ for how to predict on longer files) 

