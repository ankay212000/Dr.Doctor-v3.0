import csv
import pandas as pd
import numpy as np
from collections import defaultdict
import os
import shutil

def start():
    try:
        os.mkdir("Disease")
    except:
        shutil.rmtree("Disease")
        os.mkdir("Disease")    
    df = pd.read_csv('./dataset/raw_data.csv')
    data = df.fillna(method='ffill')

    def process_data(data):
        data_list = []
        data_name = data.replace('^','_').split('_')
        n = 1
        for names in data_name:
            if (n % 2 == 0):
                data_list.append(names)
            n += 1
        return data_list

    disease_list = []
    disease_symptom_dict = defaultdict(list)
    disease_symptom_count = {}
    count = 0

    for idx, row in data.iterrows():
    
        # Get the Disease Names
        if (row['Disease'] !="\xc2\xa0") and (row['Disease'] != ""):
            disease = row['Disease']
            disease_list = process_data(data=disease)
            count = row['Count of Disease Occurrence']

        # Get the Symptoms Corresponding to Diseases
        if (row['Symptom'] !="\xc2\xa0") and (row['Symptom'] != ""):
            symptom = row['Symptom']
            symptom_list = process_data(data=symptom)
            for d in disease_list:
                for s in symptom_list:
                    disease_symptom_dict[d].append(s)
                disease_symptom_count[d] = count

    df1 = pd.DataFrame(list(disease_symptom_dict.items()), columns=['Disease','Symptom']) 
    df1.to_csv('Cleaned_data.csv')

    x=df1.loc[:,'Symptom']
    y=df1.loc[:,"Disease"]
    for i in range(149):
        filename=y[i]+".csv"
        x[i].append("percentage")
        disease=x[i]
        with open('./Disease/'+filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(disease)

start()            