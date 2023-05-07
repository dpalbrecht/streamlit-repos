import streamlit as st



def load_css():
    st.set_page_config(layout="wide")
    margins_css = """
    <style>
        .main > div {
            padding-top: 2rem;
        }
        div.h1 {
            font-size: 30px;
            font-weight: bold;
            text-align: center;
        }
        div.h4 {
            font-size: 15px;
            text-align: center;
            padding-bottom: 50px;
        }
        div.message {
            font-size: 50px;
            text-align: center;
            font-weight: bold;
        }
        div.submessage {
            font-size: 30px;
            text-align: center;
        }
        div.stButton {
            padding-left: 30%;
        }
        .stButton button {
                border: 1px solid transparent;
                font-size: 30px;
                border-radius: 0.25rem;
                color: #fff;
                background-color: #007bff;
                border-color: #007bff;
                text-align: center;
                width: 60%;
            }
        .stButton button:hover {
            border: 1px solid transparent;
            font-size: 30px;
            border-radius: 0.25rem;
            color: #fff;
            background-color: #383;
            border-color: #007bff;
        }
        .stButton button:focus {
                color: #fff !important;
                border-color: #007bff !important;
                box-shadow: none;
            }
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
    </style>
    """
    st.markdown(margins_css, unsafe_allow_html=True)
