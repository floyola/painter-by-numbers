# Reconocimiento de Pinturas usando Redes Neuronales Convolucionales


## Conjunto de Datos

El conjunto de imágenes que se utilizó para este proyecto forma parte de una competencia de **Kaggle** [https://www.kaggle.com/c/painter-by-numbers/data] el cual puede ser descargado desde la linea de comandos teniendo una cuenta de Kaggle.

```
pip install -q kaggle
mkdir -p ~/.kaggle
cp kaggle.json ~/.kaggle/
ls ~/.kaggle
chmod 600 ~/.kaggle/kaggle.json

#Download All Kaggle DataSet
kaggle competitions download -c painter-by-numbers -p ./data/
```
### Si solo queremos descargar los archivos mas relevantes ejecutamos lo siguiente:
```
kaggle competitions download -c painter-by-numbers -f train.zip -p ./data/
unzip -nq train.zip
kaggle competitions download -c painter-by-numbers -f test.zip #-p ./data/
unzip -nq test.zip
```

### Si queremos hacer uso del conjunto de imágenes ya procesadas ejecutamos lo siguiente:
```
wget https://github.com/zo7/painter-by-numbers/releases/download/data-v1.0/train.tgz -P ./data/
tar -zxf train.tgz -C ./data
wget https://github.com/zo7/painter-by-numbers/releases/download/data-v1.0/test.tgz -P ./data/
tar -zxf test.tgz -C .data
```

### Descargamos el archivo .csv donde viene la información de las imágenes 
```
kaggle competitions download -c painter-by-numbers -f all_data_info.csv.zip -p ./data/
unzip -nq all_data_info.csv.zip -d ./data
```
### Finalmente movemos todas las imágenes a un mismo directorio

```
mkdir dataset/
find test/ -name "*.jpg" -exec mv {} dataset/ \;
find train/ -name "*.jpg" -exec mv {} dataset/ \;
```
## Jupyter Notebooks

### En el directorio ```data``` se encuentran un archivo relevantes:

 - Data.ipynb  -> Notebook que contiene los comandos para crear directorios de imágenes filtrados por artistas, estilos o géneros específicos.

### En el directorio ```src``` se encuentran tres archivos relevantes:

 - Train_Models.ipynb  -> Notebook que contiene los comandos para crear y entrenar a un modelo.
 - Evaluate_Models.ipynb -> Notebook que contiene los comandos para medir la precisión de un modelo.
 - data.py -> Archivo que contiene un método que regresa una instancia de un DataLoader

### En los directorios ```src/AlexNet``` y ```src/ResNet```  se encuentras varios modelos entrenados.
