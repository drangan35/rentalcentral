import streamlit as st
import datetime
import pandas as pd
from csv import writer

master_list = []
product_offering = ["Bobcat S185 Skidloader", "John Deere 315 Backhoe", "NorthStar Stump Grinder", "2017 Peterbilt 389"]

def datacollection():
    name = st.text_input("Full Name")
    product = st.selectbox("Product", product_offering)
    insurance = st.selectbox("Insurance", ["Yes", "No"])
    start = st.date_input("Start Date", datetime.date.today(), key="start")
    end = st.date_input("End Date", datetime.date.today() + datetime.timedelta(days=1), key="end")
    if start >= end:
        st.error("Start Date Cannot Be After End Date")
    info = st.slider("Cost Per Day", min_value=0, max_value=None)
    submit = st.button("Enter")
    if submit:
        addition = [name, product, insurance, start, end, info]
        save_data(addition)

def save_data(list):
    file = open('data123.csv', 'a')
    file.write("\n" + str(list[0]) + "," + str(list[1]) + "," + str(list[2]) + "," + str(list[3]) + "," + str(list[4]) + "," + str(list[5]))


def search_data():
    df = pd.read_csv('data123.csv')
    product_select = st.selectbox("Filter By Product", product_offering)
    insurance_select = st.selectbox("Filter By Insurance", df['Insurance'].drop_duplicates())
    cost_select = st.slider("Filter By Cost")
    st.dataframe(df[(df.Product == product_select) & (df.Insurance == insurance_select) & (df.Cost <= cost_select)])
    st.markdown("""---""")
    st.write("To Submit An Inquiry, Please Leave Your Email And Desired Product ID Number")
    id = st.selectbox("ID Numbers", df.index.tolist())
    email = st.text_input("Email Address")
    if '@' not in email:
        st.error("Enter a Valid Email")
    submission = st.button("Submit")






def main():
    page = st.sidebar.selectbox("Navigation", ["Enter Your Equipment", "Request Equipment", "Meet The Team"])
    if page == "Enter Your Equipment":
        st.title("Rental Central")
        datacollection()
    if page == "Request Equipment":
        st.title("Rental Central")
        search_data()
    if page == "Meet The Team":
        st.image('venopic.jpeg', caption='Owner/CEO/CFO/CWO')
        st.image('dhruvpic.jpeg', caption='Local Guy')



main()

