import pandas as pd
import time
import os
import shutil

data = pd.read_csv('all_data_info.csv')

def sample(type='artist', min_bound=400, max_bound=500, limit_samples=5):
    '''Function that creates test,valid and train folder to provides as a argument for        a DataLoader 
      Paramaters:
        type -> Principal atribute of the dataset(ie. artist, style, genre, etc)
        min_bound -> The min bound of samples of the class
        max_bound -> The max bound of samples of the class
        limit_samples -> Classes limit
       Return:
           None
      
    '''
    mapping = {}
    total = 0
    images = 0

    for elem in data[type].value_counts().iteritems():
        samples = elem[1]
        if (samples >= min_bound and samples <= max_bound and total < limit_samples):
            mapping[elem[0]] = elem[1]
            total += 1
            images += elem[1]

    print ()
    print ("Classes: " , total , "\nImages: ", images)

    for elem in mapping.keys():
        samples = {}
        samples['train'] = round(mapping[elem]*0.8)
        samples['valid'] = round(mapping[elem]*0.1)
        samples['test'] = round(mapping[elem]*0.1)
        mapping[elem] = samples

    try:
        os.mkdir(F'./{limit_samples}/')
    except:
        pass
    try:
        os.mkdir(F'./{limit_samples}/{type}')
        os.mkdir(F'./{limit_samples}/{type}/train')
        os.mkdir(F'./{limit_samples}/{type}/valid')
        os.mkdir(F'./{limit_samples}/{type}/test')
    except:
        pass

    for index, elem in data.iterrows():
        if elem[type] in mapping:
            name = elem[type]
            file = elem['filename']
            folder = None
            if mapping[name]['train'] > 0:
                folder = 'train'
                mapping[name]['train'] -= 1
            elif mapping[name]['valid'] > 0:
                folder = 'valid'
                mapping[name]['valid'] -= 1
            else:
                folder = 'test'
                mapping[name]['test'] -= 1
            target = F'./{limit_samples}/{type}/{folder}/{name}/{file}'
            source = F'./dataset/{file}'
            try:
                shutil.copyfile(source, target)
            except FileNotFoundError:
                os.mkdir(F'./{limit_samples}/{type}/{folder}/{name}/')
                shutil.copyfile(source, target)
