# Autocomplete_shiny
 Clinically relevant predictive- autocomplete using R shiny.
 
 Motivation of project:
 Although autocomplete is already very widely used, it has a relatively high error rate in the medical domain due to not being specifically trained and optimized on medical datasets. As an example, standard autocomplete implemented by Google and other search engines does not support ICD-10 and Human phenotype ontology terms and codes. 
Autocomplete is useful in the medical domain because it ensures that a user does not need to type an entire complex medical term from memory which can be prone to misspellings and other typographical errors. 
 
 Information on the provided folders:
 
Datasets: This folder shows the ICD10 and HPO databases used. The MIMICIII databases used are not provided because they are not available for public distribution without authorisation ( a person must take the online course before gaining access to those datasets.)
 
Flask API stuff : This folder contains the code written for the three different Flask APIs for the three different autocompletion cases (for single word autocompletion, bigrams (two consecutive words) and entire queries. It also imports the Tries search algorithm written in Python. 

Jupyter Notebooks: This folder contains all the Jupyter Notebooks used for the different purposes for the project.  

Shiny APP: R shiny code used to design a prototype autocomplete input field.

