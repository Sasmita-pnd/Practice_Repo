import streamlit as st

st.title("Practice Webapp using Streamlit")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")

#header
#subheader

agree = st.checkbox("I agree")

if agree:
    st.write("Great Practice!")

st.header("Radio Button")
genre = st.radio(
    "What's your Favourite",
    ["Comedy", "Drama", "Documentary"],
    
)

if genre == "Comedy":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")