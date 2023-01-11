import streamlit as st

st.set_page_config(page_title="Hello",layout="wide")
st.title("Silver Bells Public School :tada:")

n=int(st.number_input("Enter any number",0))
clicked=st.button("Click on me")
if clicked:
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        st.info("Number is prime")
        st.number_input.clear()
    else:
        st.info("Number is not prime")
        st.number_input.clear()

