import joblib
import pandas as pd

def get_user_input():
    input_data = {}
    input_data['StockOptionLevel'] = int(input("Stock Option Level: "))
    input_data['TotalWorkingYears'] = int(input("Total Working Years: "))
    input_data['Age'] = int(input("Age: "))
    input_data['JobLevel'] = int(input("Job Level: "))
    input_data['MonthlyIncome'] = int(input("Monthly Income: "))
    input_data['YearsWithCurrManager'] = int(input("Years With Current Manager: "))
    input_data['YearsInCurrentRole'] = int(input("Years In Current Role: "))
    return input_data

def make_prediction(input_data):
    model = joblib.load('logreg_model.joblib')

    feature_names = ['StockOptionLevel', 'TotalWorkingYears', 'Age', 'JobLevel', 'MonthlyIncome','YearsWithCurrManager', 'YearsInCurrentRole']
    input_df = pd.DataFrame([input_data], columns=feature_names)

    prediction = model.predict(input_df)
    return prediction[0]

user_input = get_user_input()
prediction_result = make_prediction(user_input)
print("=====================================")
print("Predicted Attrition:", "Yes or 1.0" if prediction_result == 1 else "No or 0.0")
print("=====================================")