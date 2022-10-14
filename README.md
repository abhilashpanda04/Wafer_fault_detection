Wine Qality Prediction with MLops and Falsk:

The aim of this project is to predict the quality of wine on a scale of 0–10 given a set of features as inputs. 

we will use the openly available dataset for wine quality  to build a machine learning model to predict the wine Qality.

the next steps will be to automate the entire machine learning pipeline with a fully function CI-CD-CT pipeline.

the front end will be then build with flask for the end users to use the application

we will also include test cases for checks before deploying the model into production.


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
