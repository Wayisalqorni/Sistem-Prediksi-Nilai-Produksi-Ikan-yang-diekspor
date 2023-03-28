import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv('data-nilai-eksport.csv')

# Set page title
st.title('Sistem Prediksi Nilai Produksi Ikan yang Diekspor')

# Set sidebar options
sidebar_options = ['Deskripsi Data', 'Prediksi']
sidebar_choice = st.sidebar.selectbox('Pilihan', sidebar_options)

# Deskripsi Data
if sidebar_choice == 'Deskripsi Data':
    st.header('Deskripsi Data')
    st.write(df.head(500))
    
# Prediksi
elif sidebar_choice == 'Prediksi':
    st.header('Prediksi Nilai Produksi Ikan yang Diekspor')
    
    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df[['produksi_(kg)']], df['nilai_($us)'], test_size=0.2, random_state=0)
    
    # Create linear regression model
    model = LinearRegression()
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Input form
    st.subheader('Masukan Data:')
    form = st.form(key='prediction_form')
    input_produksi = form.number_input('Produksi (Kg)', min_value=0, max_value=1000000, step=1000, value=1)
    submit_button = form.form_submit_button(label='Submit')
    
    # Make prediction
    if submit_button:
        y_pred = model.predict([[input_produksi]])
    
        # Output result
        st.subheader('Hasil Prediksi')
        st.write(f'Nilai Produksi yang Diekspor (satuan dalam US dolar):   ${round(float(y_pred), 2)} US')
