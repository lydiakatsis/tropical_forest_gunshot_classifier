# Tropical forest gunshot classifier

Reproducability code for Katsis, L. K. D., et al. (2022). "Automated detection of gunshots in tropical forests using convolutional neural networks." Ecological Indicators 141 doi: https://doi.org/10.1016/j.ecolind.2022.109128

This associated data used for model training and validation (749 gunshots, and 35239 background sounds collected in tropical forest sites in Belize) is archived on Mendeley Data doi: https://doi.org/10.17632/x48cwz364j.3 

For detailed information and instructions on how to run predictions using this model, see the [Opensoundscape docs](http://opensoundscape.org/en/latest/index.html).

Requirements:
- Python 3.7
- Opensoundscape

# Quick start
Classify files using the Google Colab script [here](https://colab.research.google.com/github/lydiakatsis/tropical_forest_gunshot_classifier/blob/main/Gunshot%20classification%20GUI/Gunshot_classifier_colab.ipynb)
* Opensoundscape 0.7.1. 

# Gunshot classification GUI #
* User-friendly scripts to run the classification algorithm on your data are found in the subfolder [Gunshot classification GUI](https://github.com/lydiakatsis/tropical_forest_gunshot_classifier/tree/main/Gunshot%20classification%20GUI)
* This page contains instructions on running the scrips, and example data.
* Opensoundscape 0.7.1

# Model training and classification #
* Scripts used to reproduce the manuscript are found in the subfolder [Model and code](https://github.com/lydiakatsis/tropical_forest_gunshot_classifier/tree/main/Model%20and%20code)
* This folder contains the training script, the final model, and the prediction script

**IMPORTANT - this model currently must be opened within Opensoundscape 0.5.0 or 0.6.0 to replicate results in paper. Results differ if opened in later versions of opensoundscape**

