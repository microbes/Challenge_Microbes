# MicroBES Challenge

Welcome to the MicroBES Challenge, here you will find all the ressources you need to start the projet !

## Data

Data needed to do the challenge is available in the **data** folder. It contains the 3 datasets in CSV and ARFF format.
* **train_set.csv**, **valid_set.csv**, **test_set.csv** are the datasets in CSV format
* **train_set.arff**, **valid_set.arff**, **test_set.arff** are the datasets in ARFF format
* **data_csv.zip** is a ZIP file containing all the CSV datasets
* **data_arff.zip** is a ZIP file containing all the ARFF datasets

We strongly recommend to use ARFF dataset if you are using Weka. Otherwise CSV files are preferred.

Files size are reported in the following table :

Filename | Size
-------- | ----
train_set.csv | 10.8 MB
valid_set.csv | 2.3 MB
test_set.csv | 2.0 MB
train_set.arff | 11.2 MB
valid_set.arff | 2.4 MB
test_set.arff | 2.1 MB
data_csv.zip | 1.7 MB (15.1 MB unzipped)
data_arff.zip | 1.8 MB (15.7 MB unzipped)

## Misc

This folder have 2 files, **example_submission.zip** which provides an exemple of how a submission should be formatted and **score.py** the score function used in the challenge.

## Starting kit

We provide a starter kit for scikit-learn (Python) and Weka (Java) :
* the scikit-learn starter kit is a ipython notebook
* the Weka starter kit contains 2 java files : **GettingStarted.java** which is a minimal working example to directly get results and see how the weka library works, **GoingFurther.java** implementing more functions and offer more options for the classifiers