# User friendly gunshot classification script

 This model can be run on a standard desktop in a Python environment such as JupyterLab Desktop, with minimal knowledge of Python programming.
 
**Gunshot detection will provide *a lot* of false positives. Therefore it is a must to verify the results. You will likely find a very small proportion of your results are true gunshots, but this process will substantially reduce the human effort needed to annotate sound files and extract gunshots.**

## FAQs ##
* **What data does the model expect?**
  * Audio files in the form of .wav or .WAV of any length (minimum 4 seconds long)
* **Can I access example files to trial to model?**
  * Yes - example data are found here. (link to be added).

## Gunshot Classification Instructions ##

* Download JupyterLab Desktop [here](https://github.com/jupyterlab/jupyterlab-desktop#download) . This software can be downloaded on Windows and Mac computers.
  * JupyterLab Desktop is a user friendly way of accessing a Python environment needed to run these scripts.
* Download the files on this page (follow instructions below to do this).
  * Files are located on the root page [here](https://github.com/lydiakatsis/tropical_forest_gunshot_classifier) and will take up ~123 Mb.
* Drag and drop the file entitled 'Gunshot classifier start here! .ipynb' into the folder containing your sound files. This script is designed to analyse one SD card at a time, so it will not recurse through multiple folder levels. 
* Double click on the file within the folder, which will open it up within Jupyter Lab Desktop.
* Follow the steps marked out on the script, and happy classifying!
 
 
*How to download the files*:

<img width="1071" alt="Screenshot 2022-08-05 at 14 38 07" src="https://user-images.githubusercontent.com/72734966/183140838-9dae6da6-0780-4768-a9fb-900c3310bed9.png">

## Gunshot Verification ##
This script allows quick filtering through the results by inspecting spectrograms and listening to sounds, and allows you to create an annotation table. It also requires JuptyterLab to open and run. 

* Make sure you have downlaoded JupyterLab Desktop.
* Drag and drop the file entitled 'Gunshot verification start here!.ipynb' into the folder containing the sound files you classified, which will also contain the results table from the gunshot classifier.
* Double click on the file within the folder, which will open it up within Jupyter Lab Desktop.
* Follow the steps on the script, which will order the results from highest score to lowest, and then play the sounds with associated spectrogram in that order, and allow you to interactively annotate with integer values.
* Once you are finished, it will save the results that you annotated into a csv labelled 'annotations.csv' in this same folder.

- Original version from Kitzes lab, at this [link](https://github.com/kitzeslab/bioacoustics-cookbook/blob/main/top-down-listening.ipynb)
