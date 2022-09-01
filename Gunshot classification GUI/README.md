# User friendly gunshot classification script

 This model can be run on a standard desktop in a Python environment such as JupyterLab Desktop, with minimal knowledge of Python programming.
 
**Gunshot detection will provide *a lot* of false positives. Therefore it is a must to verify the results. You will likely find a very small proportion of your results are true gunshots, but this process will substantially reduce the human effort needed to annotate sound files and extract gunshots.**

## Installing JupyterLab Desktop ##
* JupyterLab Desktop is a user friendly way of accessing a Python environment needed to run these scripts.
* Download JupyterLab Desktop [here](https://github.com/jupyterlab/jupyterlab-desktop#download) . This software can be downloaded on Windows and Mac computers.
 * Once you have downloaded JupyterLab, the first time you open the program you will get a pop-up saying 'Set Python Environment'. Select the option saying 'Install Python environment using the bundled installer', and then select 'Apply and restart'
 * This will take you to a new installation pop-up - progress through this pop-up. There is no need to select anything additional on these pages apart from the defaults that are already selected. Once you have done this, it may take a few minutes to install the environment.
![184942600-ee3a72e5-928c-4056-b745-d9bee43ff03b](https://user-images.githubusercontent.com/72734966/184943507-c7ea33f6-062b-4fc1-a980-7a6acd75c6fa.png)


## Gunshot Classification Instructions ##
* Download the files on this page (follow instructions below to do this).
  * Files are located on the root page [here](https://github.com/lydiakatsis/tropical_forest_gunshot_classifier) and will take up ~123 Mb.
* Drag and drop the file entitled 'Gunshot classifier start here! .ipynb' into the folder containing your sound files. 
  * This script is designed to analyse one SD card at a time, so it will not recurse through multiple folder levels. 
  * File format must be .WAV or .wav
  * Files of any length can be classified
* Double click on the file within the folder, which will open it up within Jupyter Lab Desktop.
* Follow the steps marked out on the script, and happy classifying!
 

## Gunshot Verification Instructions ##
This script allows quick filtering through the results by inspecting spectrograms and listening to sounds, and allows you to create an annotation table. It also requires JuptyterLab to open and run. 

* Make sure you have downlaoded JupyterLab Desktop.
* Drag and drop the file entitled 'Gunshot verification start here!.ipynb' into the folder containing the sound files you classified, which will also contain the results table from the gunshot classifier.
* Double click on the file within the folder, which will open it up within JupyterLab Desktop.
* Follow the steps on the script, which will order the results from highest score to lowest, and then play the sounds with associated spectrogram in that order, and allow you to interactively annotate with integer values.
* Once you are finished, it will save the results that you annotated into a csv labelled 'annotations.csv' in this same folder.

- Original version from Kitzes lab, at this [link](https://github.com/kitzeslab/bioacoustics-cookbook/blob/main/top-down-listening.ipynb)


## FAQs ##
* **What data does the model expect?**
  * Audio files in the form of .wav or .WAV of any length (minimum 4 seconds long)
* **The script doesn't open in JupyterLab Desktop - help!**
  * If this happens - you must right-click the .ipynb file and change the default program your computer opens it with.
* **How good is the classifier?**
  *  The classifier has been trained and tested specifically on sounds collected in tropical forests of Belize. It has been designed to give high recall (it shouldn't miss many gunshots), but at the cost of lower precision (there will be false positives). Therefore this classifier should be used to reduce a vast dataset into a smaller more manageable selection of files for manual review. Performance on data collected in different environments is unknown.
* **Can I access example files to trial to model?**
  * Yes - example data are found here. (link to be added).
* **How do I download the files from this page?**
  * Files are located on the root page [here](https://github.com/lydiakatsis/tropical_forest_gunshot_classifier). Click 'Code' and then 'Download zip'
  * <img width="700" alt="Screenshot 2022-08-05 at 14 38 07" src="https://user-images.githubusercontent.com/72734966/183140838-9dae6da6-0780-4768-a9fb-900c3310bed9.png">
