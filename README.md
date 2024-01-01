
#  Titanic Prediction Pipeline Project

This project is built over the most infamous **_titanic dataset_**. This project is a complete end-to-end machine learning project.

The development of the machine learning model is done in 5 different stages. This project is deployed using Streamlit.

## 🛣️ Development Stages

1. **Data Ingestion Stage**
_Ingesting the dataset from the souce URL provided._

2. Data Validation Stage
_Checking the structure of the ingested dataset, and validating it.Based on the validation, a validation file is generated saving the reference of the result of validation._

3. Data Transformation Stage
_Transforming the dataset to be feed into the model._

4. Model Training Stage
_Modeling various machine learning algorithms and then passing the dataset thorugh the model for training the model._

5. Model Evaluation Stage
_After the model has been trained, evaluating the model based on the unknown dataset and then evaluating the accuracy of the model._
 ## ⚒️ Workflows

 1. Update config.yaml
 2. Update parmas.yaml
 3. Update entity
 4. Update the configuration manager in the src config
 5. Update the components
 6. Update the pipeline
 7. Update the main.py
 8. Update the app.py
## ⚙️ Tech Stack

**Programming Language:** Python

**Package used:** Scikit-Learn, DVC (Data-Version-Control), Pandas, Numpy, Matplotlib, Seaborn, Streamlit, Scipy, Flask, pyYAML, catBoost, ensure, python_box

## 💻 How to run?

#### **STEPS,-**

**Step 1:** Clone this repository
```bash
https://github.com/krishanwalia30/Titanic_Pipeline_Project
```

**Step 2:** Create a conda environment inside the repository
```bash
conda create -n titanic python=3.9 -y
```
```bash
conda activate titanic
```

**Step 3:** Install the requirements
```py
pip install -r requirements.txt
```
```py
# Finally run the following command
python streamlit_app.py
```

**Step 4:** See the project running

```bash
open the link in the terminal [usually at port 8501]
```
## 📏 Outcome

- Learned to create an end-to-end machine learning pipeline.
- Created different modules and components for different stages in pipeline development
- Learned about Data Version Control (DVC)
- Integrated DVC with the project to make it more efficient.
- Learned to create a Flask webapp for the model.
- Discovered the functionalities of Streamlit.
- Deployed the webapp successfully on Streamlit.
- Developed Continuous Integration and Development pipeline.
## ⭐ Features

- Machine learning model with an accurcy of __93.475__
- Live Prediction, in minimum time.
- Train Endpoint integration on the webapp



## 🚀 Deployment

The project is deployed as a webapp using Streamlit
Link: https://titanicpipelineproject123.streamlit.app/


## 📑 Appendix


#### Running the DVC:
Run the following command in the main project command prompt,-
```py
dvc init
dvc repro
```