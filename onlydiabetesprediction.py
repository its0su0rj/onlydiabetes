


from streamlit_option_menu import option_menu

import numpy as np
import pickle
import streamlit as st


# loading the saved model
#loaded_model = pickle.load(open('C:/Users/sujee/Downloads/mineproject/trained_model.sav', 'rb'))
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

def diabetes_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return'The person is not diabetic'
    else:
      return'The person is diabetic'
      
def main():
    with st.sidebar:
        selected = option_menu('DIABETES and SALARYCTC PREDICTION',
                               ['DIABETES PREDICTION','SALARY PREDICTION','ITS_SU_RJ'],
                               icons=['activity','currency-rupee','emoji-heart-eyes'],
                               default_index=0)
    #diabetes prediction page
    if (selected=='DIABETES PREDICTION'):
        st.title('Diabetes prediction using SVM')

        #getting the input data from user

        Pregnancies = st.text_input('number of Pregnancies')
        Glucose = st.text_input('glucose level')
        BloodPressure = st.text_input('blood pressure value')
        SkinThickness = st.text_input('skin thickness value')
        Insulin = st.text_input('insulin level')
        BMI = st.text_input('bmi value')
        DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction value')
        Age= st.text_input('age value')

        #code for prediction
        diagnosis = ''

        #creating a button for prediction
        if st.button('diabetes test result'):
            diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
            
        st.success(diagnosis)
        
        
    if (selected=='ITS_SU_RJ'):
            st.title('THANK   YOU')
            
        
if __name__ == '__main__':
        main()
        