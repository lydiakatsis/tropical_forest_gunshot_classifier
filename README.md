# Tropical forest gunshot classifier

Reproducability code for Katsis, L. K. D., et al. (2022). "Automated detection of gunshots in tropical forests using convolutional neural networks." Ecological Indicators 141 doi: https://doi.org/10.1016/j.ecolind.2022.109128

This associated data used for model training and validation (749 gunshots, and 35239 background sounds collected in tropical forest sites in Belize) is archived on Mendeley Data doi: https://doi.org/10.17632/x48cwz364j.3 

All scripts and workflow in this repo are based heavily on OpenSoundscape 0.5.0 http://opensoundscape.org/en/latest/, created by the Kitzes Lab at the University of Pittsburgh.

Requirements:
- Python 3.7
- Opensoundscape 0.5.0

# Gunshot classification GUI #
* A user friendly and simplified jupyter notebook has been provided that easily allows you to classify your sound files. Reccomended to download Jupyter Lab Desktop and run the program from there.


# Model training and classification #
* Scripts used to reproduce the manuscript are found in the subfolder [Model and code] https://github.com/lydiakatsis/tropical_forest_gunshot_classifier/tree/main/Model%20and%20code
* This folder contains the training script, the final model, and the prediction script


