import requests
import streamlit as st


API_KEY = st.secrets["API_KEY"]["API_KEY"]

def get_data(location, fore_days):
    url = ("http://api.openweathermap.org/data/2.5/forecast?"
           f"q={location.replace(' ', '%20')}"
           f"&appid={API_KEY}")

    response = requests.get(url)
    content = response.json()
    data = content['list']
    nr_values = 8 * fore_days
    filtered_data = data[:nr_values]
    return filtered_data



if __name__ == "__main__":
    get_data('jaipur', 5, 'sky')