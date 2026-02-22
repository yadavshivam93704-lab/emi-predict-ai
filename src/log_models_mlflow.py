import os
import joblib
import mlflow
import mlflow.sklearn

# Set experiment
mlflow.set_experiment("EMI_Predict_AI")

# Resolve project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
models_path = os.path.join(BASE_DIR, "models")

with mlflow.start_run(run_name="Final_Production_Models"):

    # Load models
    rf_clf = joblib.load(os.path.join(models_path, "rf_classifier.pkl"))
    xgb_clf = joblib.load(os.path.join(models_path, "xgb_classifier.pkl"))
    log_clf = joblib.load(os.path.join(models_path, "logistic_classifier.pkl"))

    lr_reg  = joblib.load(os.path.join(models_path, "linear_regressor.pkl"))
    rf_reg  = joblib.load(os.path.join(models_path, "rf_regressor.pkl"))
    xgb_reg = joblib.load(os.path.join(models_path, "xgb_regressor.pkl"))

    # Log models (new syntax)
    mlflow.sklearn.log_model(rf_clf, name="rf_classifier")
    mlflow.sklearn.log_model(xgb_clf, name="xgb_classifier")
    mlflow.sklearn.log_model(log_clf, name="logistic_classifier")

    mlflow.sklearn.log_model(lr_reg,  name="linear_regressor")
    mlflow.sklearn.log_model(rf_reg,  name="rf_regressor")
    mlflow.sklearn.log_model(xgb_reg, name="xgb_regressor")

    # Log metadata
    mlflow.log_param("project", "EMIPredict AI")
    mlflow.log_param("total_models_logged", 6)

print("✅ All 6 models successfully logged to MLflow!")
