import streamlit as st
import pandas as pd
import pickle

# Streamlit app
st.title("Entrepreneurial Competence Prediction App")

# Set background color
st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
        }
    </style>
    """,
    unsafe_allow_html=True
)
with open('best_model-4.pkl', 'rb') as file:
    model = pickle.load(file)

# Header image
header_image = st.image("AI_image.png", use_column_width=True)

# Sidebar with user input
st.sidebar.header("To the best of your ability, fill the following fields...")

# Load the pre-trained model


# Input fields for user data
# Input fields for user data
Perseverance = st.slider("Your perseverance", min_value=0, max_value=5)
DesireToTakeInitiative = st.slider("Your Desire To Take Initiative", min_value=0, max_value=5)
Competitiveness = st.slider("Your Competitiveness", min_value=0, max_value=5)
SelfReliance = st.slider("Your Self Reliance", min_value=0, max_value=5)
StrongNeedToAchieve = st.slider("Strong Need To Achieve", min_value=0, max_value=5)
SelfConfidence = st.slider("Your Self Confidence", min_value=0, max_value=5)
GoodPhysicalHealth = st.slider("Your Physical Health", min_value=0, max_value=5)
IndividualProject = st.selectbox("Your Individual Project", ["Yes", "No"])
Influenced = st.selectbox("Influenced", ["Yes", "No"])
MentalDisorder = st.selectbox("MentalDisorder", ["Yes", "No"])
KeyTraits = st.selectbox("KeyTraits", ['Passion', 'Vision', 'Resilience', 'Work Ethic','Positivity']
)

# Gathering input data into a dictionary
input_data = {
    'Your Perseverance': Perseverance,
    'Your Desire To Take Initiative': DesireToTakeInitiative,
    'Your Competitiveness': Competitiveness,
    'Your Self Reliance': SelfReliance,
    'Your Strong Need To Achieve': StrongNeedToAchieve,
    'Your Self Confidence': SelfConfidence,
    'Your Physical Health': GoodPhysicalHealth,
    'Your Individual Project': IndividualProject,
    'Influenced': Influenced,
    'MentalDisorder': MentalDisorder,
    'KeyTraits': KeyTraits
}

# Button for making predictions
predict =st.button("Predict Entrepreneurial Competence")
reset = st.button('Reset')
if predict:
    input_data_df = pd.DataFrame(input_data, index=[0])

    # Factorize categorical columns
    cat_columns = input_data_df.select_dtypes(include=['object']).columns
    for column in cat_columns:
        input_data_df[column] = pd.factorize(input_data_df[column])[0]

    # Make prediction
    prediction = model.predict(input_data_df)

    # Display prediction result
  
    if prediction.shape[1] > 1:
    # Assuming binary classification, extract the probability of class 1
         EC_prediction = (1-prediction[0][1])
    else:
    # If only one class, use the probability of that class
        EC_prediction = (1-prediction[0][0])
    st.success(f"Your predicted Entrepreneurial competence is: {EC_prediction*100:.2f}%")
    if EC_prediction*100<= 75:
       st.warning("Your predicted Entrepreneurial competence is below 75%.")
       st.write("Your competence is average. Consider checking areas like perseverance, your desire to achieve, and self-reliance, self confidence to improve your enterprenuerial competence, and work ethics. Its not late to become your better self")
    else:
        st.success("Congratulations! Your predicted Entrepreneurial competence is above 75%.")
        st.write("You have a higher competence, keep working on your self, you are on the right path, and you are encouraged to start entrepreneurship as soon as you can.")

