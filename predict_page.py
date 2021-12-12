import streamlit as st
import pickle
import numpy as np


filename = 'ML_Admission_final.pkl'
loaded_model = pickle.load(open(filename, 'rb'))

def show_predict_page():
    st.title("Chances of Admission Prediction")

    st.write("""### please fill all below information to predict your chances for admission""")
    st.write("""#### By Ahmed B. Darwish""")
    st.write("""abdarwish@outlook.com""")

    GRE_Score = st.number_input("GRE_score")
    TOEFL_Score = st.number_input("TOEFL_score")
    University_Rating = st.number_input("Univ_Rating")
    SOP  = st.number_input("SOP")
    LOR_ = st.number_input("LOR")
    CGPA = st.number_input("CGPA")
    res = ("YES","NO")
    is_research = st.selectbox("Research", res)
    if (is_research == 'YES'):
        research = 1
    else:
        research = 0



    ok = st.button("predict_Admission")
    if ok:
        user_values = [[GRE_Score, TOEFL_Score, University_Rating, SOP, LOR_, CGPA, research]]
        prediction = loaded_model.predict(user_values)
        pred = round((float(prediction)*100),2)
        st.subheader(f"The chances of admission is equal to {pred}%")

