# Tropical forest gunshot classifier

Reproducability code for Katsis, L. K. D., et al. (2022). "Automated detection of gunshots in tropical forests using convolutional neural networks." Ecological Indicators 141 doi: https://doi.org/10.1016/j.ecolind.2022.109128

This associated data used for model training and validation (749 gunshots, and 35239 background sounds collected in tropical forest sites in Belize) is archived on Mendeley Data doi: https://doi.org/10.17632/x48cwz364j.3 

All scripts and workflow in this repo are based heavily on [OpenSoundscape 0.6.0](https://github.com/kitzeslab/opensoundscape) created by the Kitzes Lab at the University of Pittsburgh.

Requirements:
- Python 3.7
- Opensoundscape 0.6.0

IMPORTANT - model currently must be opened without Opensoundscape 0.6.0 else weights don't load correctly.


# Model training and classification #
* Scripts used to reproduce the manuscript are found in the subfolder [Model and code](https://github.com/lydiakatsis/tropical_forest_gunshot_classifier/tree/main/Model%20and%20code)
* This folder contains the training script, the final model, and the prediction script



# Gunshot classification GUI #
* User-friendly scripts to run the classification algorithm on your data are found in the subfolder [Gunshot classification GUI]
* This page contains instructions on running the scrips, and example data.
