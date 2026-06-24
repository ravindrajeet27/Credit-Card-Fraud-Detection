# Credit Card Fraud Detection System

## Overview

This project uses Machine Learning to detect fraudulent credit card transactions. The model is trained on a highly imbalanced dataset and uses Random Forest along with SMOTE (Synthetic Minority Oversampling Technique) to improve fraud detection performance.

## Features

* Data preprocessing and cleaning
* Handling class imbalance using SMOTE
* Random Forest Classification
* Hyperparameter tuning using GridSearchCV
* Model evaluation using Precision, Recall, F1-Score, and Confusion Matrix
* Streamlit web application for real-time predictions

## Dataset

The dataset contains credit card transactions with the following features:

* Time
* V1 to V28 (PCA-transformed features)
* Amount
* Class (0 = Genuine, 1 = Fraud)

Dataset Size: 284,807 transactions

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Imbalanced-learn (SMOTE)
* Joblib
* Streamlit

## Model Performance

| Metric    | Value |
| --------- | ----- |
| Precision | 61%   |
| Recall    | 89%   |
| F1-Score  | 72%   |

## Project Structure

```text
FRAUD_DETECTION/
│
├── app.py
├── fraud_detection_model.joblib
├── scaler.joblib
├── requirements.txt
├── credit_card.ipynb
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

## Future Improvements

* XGBoost implementation
* Batch prediction using Excel files
* Cloud deployment using AWS
* Model monitoring and logging

## Author

Ravindrajeet Gautam
live link : https://ravindrajeet27-credit-card-fraud-detection-app-usroav.streamlit.app/

GitHub: https://github.com/ravindrajeet27

LinkedIn: https://www.linkedin.com/in/ravindrajeet-gautam-a22053140/
