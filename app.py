import streamlit as st
from css import load_css; load_css()



st.write("<div class=h1>Welcome to the Bark Analyzer!</div>", unsafe_allow_html=True)
st.write("<div class=h4>For when your dog is talking at you and you want to know what it all means.</h4>", unsafe_allow_html=True)
cols = st.columns([2,1,2])
with cols[1]:
    clicked = st.button("What's my dog saying?")
# if clicked:
#     display_similar_products()
