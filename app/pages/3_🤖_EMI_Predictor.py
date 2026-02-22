import streamlit as st
import pandas as pd
import mlflow.pyfunc

# -----------------------------
# LOAD MODELS FROM MLFLOW
# -----------------------------
eligibility_model = mlflow.pyfunc.load_model("models:/EMI_Eligibility_Model/1")
emi_model = mlflow.pyfunc.load_model("models:/Max_EMI_Model/1")

st.title("🤖 EMI Prediction Engine")

# -----------------------------
# USER INPUTS
# -----------------------------
salary = st.number_input("Monthly Salary", 1000, 500000, 50000)
expenses = st.number_input("Total Monthly Expenses", 0, 300000, 10000)
credit = st.number_input("Credit Score", 300, 900, 700)
current_emi = st.number_input("Current EMI", 0, 100000, 0)
bank_balance = st.number_input("Bank Balance", 0, 10000000, 50000)
loan_amount = st.number_input("Requested Loan Amount", 1000, 10000000, 100000)
tenure = st.number_input("Requested Tenure (months)", 1, 360, 24)

# -----------------------------
# PREDICT BUTTON
# -----------------------------
if st.button("Predict"):

    # -----------------------------
    # FEATURE ENGINEERING
    # -----------------------------
    disposable_income = salary - expenses - current_emi
    total_expenses = expenses + current_emi

    debt_to_income = total_expenses / salary if salary else 0
    expense_to_income = expenses / salary if salary else 0
    savings_ratio = bank_balance / salary if salary else 0
    emi_burden_ratio = current_emi / salary if salary else 0

    # dummy risk score
    risk_score = (
        (1 - min(credit/900,1)) * 0.4 +
        debt_to_income * 0.3 +
        emi_burden_ratio * 0.3
    )

    # -----------------------------
    # BUILD FULL FEATURE ROW
    # ALL TRAINING COLUMNS INCLUDED
    # -----------------------------
    data = {
        'age': 30,
        'gender': 0,
        'marital_status': 0,
        'education': 1,
        'monthly_salary': salary,
        'employment_type': 1,
        'years_of_employment': 5,
        'company_type': 1,
        'house_type': 1,
        'monthly_rent': 0,
        'family_size': 3,
        'dependents': 1,
        'school_fees': 0,
        'college_fees': 0,
        'travel_expenses': 0,
        'groceries_utilities': expenses,
        'other_monthly_expenses': 0,
        'existing_loans': 1 if current_emi > 0 else 0,
        'current_emi_amount': current_emi,
        'credit_score': credit,
        'bank_balance': bank_balance,
        'emergency_fund': bank_balance * 0.2,
        'emi_scenario': 1,
        'requested_amount': loan_amount,
        'requested_tenure': tenure,
        'total_expenses': total_expenses,
        'debt_to_income_ratio': debt_to_income,
        'expense_to_income_ratio': expense_to_income,
        'disposable_income': disposable_income,
        'savings_ratio': savings_ratio,
        'emi_burden_ratio': emi_burden_ratio,
        'risk_score': risk_score
    }

    input_df = pd.DataFrame([data])

    # -----------------------------
    # FORCE TRAINING FEATURE ORDER
    # (CRITICAL FIX)
    # -----------------------------
    feature_order = [
        'age','gender','marital_status','education','monthly_salary',
        'employment_type','years_of_employment','company_type','house_type',
        'monthly_rent','family_size','dependents','school_fees','college_fees',
        'travel_expenses','groceries_utilities','other_monthly_expenses',
        'existing_loans','current_emi_amount','credit_score','bank_balance',
        'emergency_fund','emi_scenario','requested_amount','requested_tenure',
        'total_expenses','debt_to_income_ratio','expense_to_income_ratio',
        'disposable_income','savings_ratio','emi_burden_ratio','risk_score'
    ]

    input_df = input_df[feature_order]

    # -----------------------------
    # PREDICT
    # -----------------------------
    try:
        eligibility = eligibility_model.predict(input_df)[0]
        max_emi = emi_model.predict(input_df)[0]

        st.success(f"Eligibility: {eligibility}")
        st.success(f"Recommended EMI: ₹{int(max_emi)}")

    except Exception as e:
        st.error("Prediction failed")
        st.exception(e)