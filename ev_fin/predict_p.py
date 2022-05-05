import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn import svm




@st.cache(allow_output_mutation=True)
def loadData():
    df = pd.read_csv("electric_vehicle_charging_station_list.csv")
    df.drop(columns='Type',inplace=True, axis=1)
    df.drop(columns='Service',inplace=True, axis=1)
    return df
    
def preprocessing(df):

    
    # categories = ['Region','State','Address','Power','Latitude','Longitude']

    # le = LabelEncoder()
    # df[categories] = df[categories].apply(le.fit_transform)
    le_region = LabelEncoder()
    le_state = LabelEncoder()
    le_address = LabelEncoder()
    le_power = LabelEncoder()

    df["Region"] = le_region.fit_transform(df["Region"])
    df["State"] = le_state.fit_transform(df["State"])
    df["Address"] = le_address.fit_transform(df["Address"])
    df["Power"] = le_power.fit_transform(df["Power"])

    X = df.drop(['PIN','No'], axis=1)
    y = df['PIN']

    # 1. Splitting X,y into Train & Test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20,random_state=0)
    return X_train, X_test, y_train, y_test, le_region,le_state,le_address,le_power

def supportvectormachine(X_train, X_test, y_train, y_test):
    lin_clf = svm.SVC(kernel='linear', degree=8)
    lin_clf.fit(X_train, y_train)
    y_pred = lin_clf.predict(X_test)
    score = accuracy_score(y_test,y_pred)*100
    

    return score, lin_clf
    

    

def show_predict_page():
    data = loadData()
    X_train, X_test, y_train, y_test, le_region, le_state, le_address, le_power= preprocessing(data)
    score, lin_clf = supportvectormachine(X_train, X_test, y_train, y_test)
    st.title("Predict your land!!")
    user_pin = st.number_input("Enter the PIN code: ")
    lon = st.number_input("Enter the longitude: ")
    lat = st.number_input("Enter the latitude: ")
    power = st.multiselect('What is the desired power output',['15 kW', '142kW', '10(3.3 kW each)'])
    landmark = st.multiselect('What is the nearby landmark',['Market', 'Office', 'Petrol Pump', 'Bank', 'Sector', 'Hospital', 'Mall', 'Metro Station', 'Garden', 'Hotel', 'Stadium', 'Parking', 'Beach', 'Airport', 'Temple', 'School', 'Restaurant', 'College'])
    state = st.text_input("Enter the state: ")
    region = st.multiselect('What is the region',['NDMC', 'CMRL', 'Maha Metro', 'Noida Authority', 'SDMC', 'NKDA', 'NRANVP', 'ANERT', 'ASCTC', 'IMC', 'UDA'])
    ok = st.button("Predict")
    if ok:
        r=region[0]
        s=state[0]
        l = landmark[0]
        p = power[0]
        X = np.array([[r,s,l,lat,lon,p]])
        X[:,0] = le_region.fit_transform(X[:,0])
        X[:,1] = le_state.fit_transform(X[:,1])
        X[:,2] = le_address.fit_transform(X[:,2])
        X[:,5] = le_power.fit_transform(X[:,5])
        X = X.astype(float)
        

        pin = lin_clf.predict(X)
        st.subheader(f"The estimation is :{pin[0]}")

    

    
