import streamlit as st
import pandas as pd
import numpy as np
import joblib
import tensorflow as tf
import seaborn as sns
import matplotlib.pyplot as plt

# create the preprocess function
def preprocessData(user_input):
    # laod all the scaler models
    scalers = {feature: joblib.load(f"model/scaler_{feature}.joblib") for feature in feature_column}
    
    # Convert to (1 for 'Yes', 0 for 'No')
    for feature in ['Tuition_fees_up_to_date', 'Scholarship_holder', 'Debtor']:
        user_input[feature] = 1 if user_input[feature] == 'Yes' else 0

    # Convert gender to (1 form Male 0 for female)
    user_input["Gender"] = 1 if user_input["Gender"] == "Female" else 0

    # Transform numerical features using the loaded scalers models
    for feature in feature_column:
        user_input[feature] = scalers[feature].transform(np.array(user_input[feature]).reshape(1, -1))[0][0]

    # return user input in dataframe format
    return pd.DataFrame(user_input, index=[0])

# predict function
def predict(model, user_input):
    prediction = model.predict(user_input)[0]
    return prediction

# Get the feature columns and label column
feature_column = [
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_1st_sem_approved',
    'Curricular_units_2nd_sem_grade',
    'Curricular_units_1st_sem_grade',
    'Tuition_fees_up_to_date',
    'Scholarship_holder',
    'Application_mode',
    'Gender',
    'Debtor',
    'Age_at_enrollment'
]

# Application mode options
application_mode_options = {
    1: '1st phase - general contingent',
    2: 'Ordinance No. 612/93',
    5: '1st phase - special contingent (Azores Island)',
    7: 'Holders of other higher courses',
    10: 'Ordinance No. 854-B/99',
    15: 'International student (bachelor)',
    16: '1st phase - special contingent (Madeira Island)',
    17: '2nd phase - general contingent',
    18: '3rd phase - general contingent',
    26: 'Ordinance No. 533-A/99, item b2) (Different Plan)',
    27: 'Ordinance No. 533-A/99, item b3 (Other Institution)',
    39: 'Over 23 years old',
    42: 'Transfer',
    43: 'Change of course',
    44: 'Technological specialization diploma holders',
    51: 'Change of institution/course',
    53: 'Short cycle diploma holders',
    57: 'Change of institution/course (International)'
}

# Set the page title
st.title("Jaya Jaya Institut Graduation Prediction App")

# Set the sidebar header
st.sidebar.header("User Input")

# Create input widgets for each feature
user_input = {}
for feature in feature_column:
    if feature == "Gender":
        user_input[feature] = st.sidebar.selectbox(f"Select {feature}", ["Male", "Female"])
    elif feature == "Curricular_units_2nd_sem_approved" or feature == "Curricular_units_2nd_sem_grade" or feature == "Curricular_units_1st_sem_grade" or feature == "Curricular_units_1st_sem_approved":
        user_input[feature] = st.sidebar.number_input(f"Enter {feature}", min_value=0.0, max_value=20.0, value=0.0)
    elif feature == "Tuition_fees_up_to_date" or feature == "Scholarship_holder" or feature == "Debtor":
        user_input[feature] = st.sidebar.selectbox(f"Select {feature}", ["Yes", "No"])
    elif feature == 'Application_mode':
        user_input[feature] = st.sidebar.selectbox(f"Select {feature}", list(application_mode_options.keys()), format_func=lambda x: application_mode_options[x])
    elif feature == 'Age_at_enrollment':
        user_input[feature] = st.sidebar.number_input(f"Enter {feature}", min_value=15.0, max_value=100.0, value=18.0)
    else:
        user_input[feature] = st.sidebar.number_input(f"Enter {feature}", value=0.0)

# if the predict button is clicked
if st.sidebar.button("Predict"):
    # Preprocess the user input
    user_input_df = preprocessData(user_input)

    # Display the user input
    st.subheader("User Input:")
    user_input_df = pd.DataFrame(user_input_df, index=[0])
    st.write(user_input_df)

    # Load the saved models and scalers
    lr_model = joblib.load("model/y_pred_lr.joblib")
    rf_model = joblib.load("model/model_rf.joblib")
    adaboost_model = joblib.load("model/model_adaboost.joblib")
    nn_model = tf.keras.models.load_model('model/neural_network_model.h5')

    # Predict the graduation
    lr_prediction = predict(lr_model, user_input_df)
    rf_prediction = predict(rf_model, user_input_df)
    adaboost_prediction = predict(adaboost_model, user_input_df)
    nn_prediction = predict(nn_model, user_input_df.values)

    # Display the predictions
    st.subheader("Predictions:")
    st.write(f"Logistic Regression Prediction: {lr_prediction * 100}% will be Graduate")
    st.write(f"Random Forest Prediction: {rf_prediction * 100}% will be Graduate")
    st.write(f"AdaBoost Prediction: {adaboost_prediction * 100}% will be Graduate")
    st.write(f"Neural Network Prediction: {nn_prediction[0] * 100}% will be Graduate")

    # max_confidence_model = max([
    #     ("Logistic Regression", lr_prediction),
    #     ("Random Forest", rf_prediction),
    #     ("AdaBoost", adaboost_prediction),
    #     ("Neural Network", nn_prediction)
    # ], key=lambda x: x[1])
    # st.subheader(f"Model with Highest Confidence:")
    # if max_confidence_model[0] == "Neural Network":
    #     st.write(f"{max_confidence_model[0]} with confidence: {max_confidence_model[1][0] * 100}% will be Graduate")
    # else:
    #     st.write(f"{max_confidence_model[0]} with confidence: {max_confidence_model[1] * 100}% will be Graduate")

    # Display the prediction scores using barplot
    st.subheader("Scores of Different Models:")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=["Logistic Regression", "Random Forest", "AdaBoost", "Neural Network"], y=[lr_prediction, rf_prediction, adaboost_prediction, nn_prediction[0]])
    plt.xlabel("Score (%)")
    plt.title("Scores of Different Models")
    st.pyplot(plt)
else:
    # Display the user input
    st.subheader("User Input:")
    user_input_df = pd.DataFrame({'nothing' : 'nothing'}, index=[0])
    st.write(user_input_df)

    st.subheader("Predictions:")
    st.write("Logistic Regression Prediction: Click the Predict Button on the sidebar to predict")
    st.write("Random Forest Prediction: Click the Predict Button on the sidebar to predict")
    st.write("AdaBoost Prediction: Click the Predict Button on the sidebar to predict")
    st.write("Neural Network Prediction: Click the Predict Button on the sidebar to predict")