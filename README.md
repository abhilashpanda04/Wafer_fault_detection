Wafer Fault Detection 
==============================

probem statement:
The inputs of various sensors for different wafers have been provided. In electronics, a wafer (also called a slice or substrate) is a thin slice of semiconductor used for the fabrication of integrated circuits.

The goal is to build a machine learning model which predicts whether a wafer needs to be replaced or not(i.e., whether it is working or not) based on the inputs from various sensors. There are two classes: +1 and -1.


```bash
conda create -n [enname] python=3.7
```
```bash
created a requirement file 
```
```bash
pip install -r requirements.txt
```
```bash
created a template.py specified all the directories and files rewuired for the project.

python template.py
```
```bash
download the data from kaggle winequality dataset
https://www.kaggle.com/rajyellow46/wine-quality/version/1
```
```bash
git int
```
```bash
dvc init
```
```bash
dvc add data_given/winequality.csv
```

```bash
git add .
```

```bash
git commit -m "first commit"
```
used to reproduce the pipeline with dvc(data version control)

```bash
dvc repro
```
used to show the metrics tracked by dvc
```bash
dvc metrics show
```
used to check old tracked metric values for the model

```bash
dvc metrics diff
```
tox commands

```bash
tox
```
```bash
tox -r
```

pytest command

```bash
pytest -v
```

setup commands-

```bash
pip install -e .
```
build your own package commands -

```bash
python setup.py sdist bdist_wheel
```
running app
```bash
python app.py
```
