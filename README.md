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
