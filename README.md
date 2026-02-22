# EMI Predict AI (FinTech Loan Intelligence System)

## 📌 Project Overview

EMI Predict AI is a machine learning system that predicts:

• Loan EMI eligibility (classification)
• Maximum affordable EMI (regression)

The system helps banks or fintech platforms evaluate whether a user can safely afford a loan based on financial behaviour and risk indicators.

---

## 🧠 Machine Learning Models Used

### Classification (Eligibility)

* Logistic Regression
* Random Forest
* XGBoost ⭐ Best model (~97% accuracy)

### Regression (Max EMI)

* Linear Regression
* Random Forest ⭐ Best model (Lowest RMSE)
* XGBoost

---

## 📊 Key Features Used

* Monthly salary
* Total expenses
* Disposable income
* Debt-to-income ratio
* Existing EMI burden
* Credit score
* Savings ratio
* Risk score

---

## ⚙️ Tech Stack

* Python
* Scikit-learn
* XGBoost
* Pandas / NumPy
* MLflow (model tracking)
* Streamlit (UI – deployment pending)

---

## 📂 Project Structure

```
app/           → Streamlit frontend
Data/          → datasets & scripts
models/        → trained models
Notebooks/     → EDA + training notebooks
src/           → MLflow logging scripts
```

---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app/app.py
```

---

## 🎓GUVI Mini Project – FinTech AI

This project is built as part of a FinTech AI system to demonstrate:

✔ Financial risk modeling

✔ Machine learning pipeline

✔ Model tracking with MLflow

✔ Loan decision automation

---

## 👨‍💻 Author

Shivam Yadav

Batch - DS-C-WE-E-B74 
