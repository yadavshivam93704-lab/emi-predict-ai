import mlflow.pyfunc

def load_models():

    models = {
        # Best classification model (XGBoost)
        "eligibility": mlflow.pyfunc.load_model(
            "models:/EMI_Eligibility_Model/1"
        ),

        # Best regression model (Random Forest)
        "max_emi": mlflow.pyfunc.load_model(
            "models:/Max_EMI_Model/1"
        )
    }

    return models
