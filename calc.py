import streamlit as st

st.header("BAsic Calculator")

def square(num):
    return num*num

num = st.number_input("Insert a number")
st.write("The current number is ", num)

#how to call this function-on demand function
if st.button("Calculate Square"):
    result=square(num)
    st.subheader(result)