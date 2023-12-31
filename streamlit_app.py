import streamlit

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Freerange egg')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


fruit_selected = pandas.DataFrame({'Fruit':["Strawberry","Avacado","Banana","Orange"]})
fruit_selected = streamlit.multiselect("Pick some fruits:", options =list(my_fruit_list.index),['Avacado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruit_selected]

streamlit.dataframe(my_fruit_list)

streamlit.header('Fruityvice fruit advice')
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
