import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

@st.cache
def load_data():
    data = pd.read_csv('electric_vehicle_charging_station_list.csv')
    data.drop(columns='Type',inplace=True, axis=1)
    return data

data = load_data()


def show_explore_page():
    st.title("EV CHarging Station")

    st.subheader("Explore the data and the inferentials")
    st.write("#")
    st.write("#")


    df = data["State"].value_counts()

    fig1,ax1 = plt.subplots()
    ax1.pie(df,labels=df.index,autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis("equal")

    st.write("##### Number of data from different states")
    st.pyplot(fig1)
    st.write("#")

    expander = st.expander("See explanation")
    expander.write("""The given pie chart explains that our dataset comprises mostly data from Delhi and Uttar Pradesh """)


    st.write("##### Number of charging stations near a Facility")
    fig = plt.figure(figsize=(12, 5))
    sb.countplot(x = "Address", data = data)
    st.pyplot(fig)
    st.write("#")
    expander1 = st.expander("See explanation")
    expander1.write("""The given figure shows us that market and offices are the places where the stations are built commonly. """)


    st.write("##### Type of chargers in accordance to each State")


    fig = plt.figure(figsize=(15,6))
    sb.countplot(x='Power',data=data, hue='State')
    plt.title('Type of chargers in accordance to each State')
    plt.xlabel('Type of charger')
    plt.ylabel('frequency')
    st.pyplot(fig)
    st.write("#")
    expander2 = st.expander("See explanation")
    expander2.write("""The given figure shows us that 15kW and 148kw are the most used as expected because 15kW is mostly applied in the cities. """)
    
    st.write("##### Type of service in accordance to each State")

    fig= plt.figure(figsize=(15,6))
    sb.countplot(x='State',data=data, hue='Address')
    plt.title('Type of service in accordance to each State')
    plt.xlabel('Type of charger')
    plt.ylabel('frequency')
    plt.legend(loc='center right', title='Address')
    st.pyplot(fig)

    st.write("#")
    expander3 = st.expander("See explanation")
    expander3.write("""The given figure gives the general demographics of the dataset. """)
    
    st.write("##### Plotted EVs")   
    map_data = pd.DataFrame()
    map_data['lat'] = data['Latitude']
    map_data['lon'] = data['Longitude']
    st.map(map_data, zoom = 14)
    expander4 = st.expander("See explanation")
    expander4.write("""The given map shows the stations scattered on the Indian map for our dataset. """)
