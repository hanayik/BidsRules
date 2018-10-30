# Introduction

The [Brain Imaging Data Structure (BIDS)](http://bids.neuroimaging.io/) organizes brain imaging data for analysis and sharing. MRI scanners typically save data in the DICOM format, whereas BIDS expects each image to be saved in the NIfTI format and to include a text file (in JSON format).

[Dcm2Bids](https://github.com/cbedetti/Dcm2Bids) uses dcm2niix to convert DICOM data into the BIDS format. It does this with a configuration file that helps detect each image, helping to discriminate different modalities like T1-weighted, fMRI and resting-state images.

FUBAR is a graphical interface for Dcm2Bids. You simply drop a folder with all of a participant's DICOM images onto FUBAR. It will show a possible conversion with its best guess as a conversion. You can then edit the rules for converting images. You can use the graphical interface for each participant, or save your rules if you want to apply it as a batch to data from many different individuals.

# Data Types

Each BIDS image requires a dataType:modalityLabel. If you set this to discard the file will not be saved (e.g. if you want to ignore localizer scans used to plan subsequent images).

Below is a list of the dataType:modalityLabel in the BIDS 1.2 specification. You can even add new ones by editing the file fubar.json (though you probably shouldn't, as other BIDS tools may not understant them).

* **anat:T1w** T1-weighted image (fat is bright)
* **anat:T2w** T2-weighted image (water is bright)
* **anat:T1rho** Quantave T1rho brain imaging
* **anat:T1map** quantitative T1 map
* **anat:T2map** quantitative T2 map
* **anat:T2star** High resolution T2** image
* **anat:FLAIR** T2-FLAIR (pathology bright)
* **anat:FLASH** FLASH
* **anat:PD** Proton density
* **anat:PDmap** Proton density map
* **anat:PDT2** Combined PD/T2
* **anat:angio** Angiography
* **func:bold** Functional imaging: T2star images used for task-based or rest imaging
* **dwi:dwi** Diffusion weighted imaging
* **discard** Images with this data type will not be saved (e.g. localizer)

# Custom Labels

customLabels is an optional field. For some acquisitions, you need to add information in the file name. For resting state fMRI, it is usally **task-rest**.

# Criteria

For each series, you will want to provide the rule for detecting this image as belonging to the specified datatype. A pull-down menu will list the possible criteria. For example, the criteria "SeriesDescription=MPRAGE_T1" might be specific to your T1 scan, while the criteria "ReceiveCoilName=Head_32" would not be a good choice because all the images from the same session will use the same receive coil (so this criteria will not discriminate between different data types.
