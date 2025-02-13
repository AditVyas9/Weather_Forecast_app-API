import streamlit as st
import plotly.express as px
import backend as bk


st.header('Weather Forecast App for the Next Days')
place = st.text_input('Place:')
days = st.slider('Forecast Days:', min_value=1, max_value=5,
                      help="Select the number of forecasted days.")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")


if place:
    try:
        filtered_data = bk.get_data(place, days)
        if option == "temperature":
            temp = [dict['main']['temp'] / 10 for dict in filtered_data]
            date = [dict['dt_txt'] for dict in filtered_data]
            figure = px.line(x=date, y=temp, labels={"x": "Dates", "y": f"Temperature({u"\u00b0"}C)"})
            st.plotly_chart(figure_or_data=figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": 'images/rain.png', "Snow": "images/snow.png"}
            sky_co = [dict[0]['weather']['main'] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_co]

            st.image(image_paths, width=115)

    except KeyError:
        st.header("This place doesn't exist.")