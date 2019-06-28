# PySpark-Dataframes-and-RDD
##PySpark Dataframes and RDD to transform data and then Topic Modelling using LDAvis and Analysis using DASH

### PySpark RDD
In the basic component of this project, we are required to load into our pyspark (In this case i used spark context in windows Jupyter notebook)
the file "enwiki-20190420-pages-articles-multistream-index.txt". This file is extremely big so it is not possible to upload this dataset to Github.

Basically, the data looks like this:  
![Rough Idea of Data, take 2 lines](https://github.com/cjy93/PySpark-Dataframes-and-RDD/blob/master/RDD/HowTheInputFileLooksLIke.PNG)  

We run through a few steps using RDD syntax (please see the .ipynb file for codes) to get the output:
[output](https://github.com/cjy93/PySpark-Dataframes-and-RDD/blob/master/RDD/rdd_output_new.txt)

However, in the RDD code there is a bag of words right before we segregate to words starting with "a","e","i","o","u". I exported the bag of words
to do **Topic Modelling* using the package LDAvis. I took only a SUBSET of the words because the number of words are too huge and takes too long to load
The output looks like this: [link to LDAVis output](https://github.com/cjy93/PySpark-Dataframes-and-RDD/blob/master/RDD/lda1.html)
[![link to my youtube video](http://img.youtube.com/vi/157-qvFV6fg/0.jpg)](http://www.youtube.com/watch?v=157-qvFV6fg)


### PySpark DataFrames
This basic requirement is to use [1903.json](https://github.com/cjy93/PySpark-Dataframes-and-RDD/blob/master/DataFrames/1903.json) dataset gotten from
[URA website](https://www.ura.gov.sg/maps/api/#private-residential-property) and go through a series of PySpark Dataframes to get 
![Top 20 unsold Private residential units](https://github.com/cjy93/PySpark-Dataframes-and-RDD/blob/master/DataFrames/top_20_unsold_private_Properties.png)

All the basic and **bonus** codes for PySpark dataframes are at [link](https://github.com/cjy93/PySpark-Dataframes-and-RDD/tree/master/DataFrames). Other than getting the top
20 unsold Private properties, i also gathered other datasets through PySpark Dataframe way before putting into DASH to create the following visualisations.  
The Dash App codes are in this folder: [Dash Apps](https://github.com/cjy93/PySpark-Dataframes-and-RDD/tree/master/DataFrames/createdData)  

Click on the youtube link for my apps visualisation.  
[![link to my youtube video](http://img.youtube.com/vi/gXq5b1p1sso/0.jpg)](http://www.youtube.com/watch?v=gXq5b1p1sso)  

Pictures of the 4 apps as follows:
![app 1](https://github.com/cjy93/PySpark-Dataframes-and-RDD/blob/master/DataFrames/createdData/app1.PNG)  
![app 2](https://github.com/cjy93/PySpark-Dataframes-and-RDD/blob/master/DataFrames/createdData/app2.PNG)  
![app 3](https://github.com/cjy93/PySpark-Dataframes-and-RDD/blob/master/DataFrames/createdData/app3.PNG)  
![app 4](https://github.com/cjy93/PySpark-Dataframes-and-RDD/blob/master/DataFrames/createdData/app4.PNG)
