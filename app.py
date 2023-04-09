import streamlit as st
from css import load_css; load_css()
import pickle
import base64
from io import BytesIO
import numpy as np


@st.cache_data
def get_recs_dict():
    return pickle.loads(open('recs.p','rb').read())


def get_row_html(data):
    buffered = BytesIO()
    data[2].save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    result = f"""
    <tr>
        <td><img src="data:image/jpeg;base64,{img_str.decode('utf8')}"/></td>
        <td>{data[0]}</td>
        <td>{data[1]}</td>
    </tr>
    """
    return result


def get_html(product_list):
    table_header = """
    <table>
    <tr>
        <th>Image</th>
        <th>Title</th>
        <th>Description</th>
    </tr>
    """
    input_product = f"""
    <h2>Input Product</h2>
    {table_header}
    {get_row_html(product_list[0])}
    </table>
    <br>
    """
    similar_products = f"""
    <h2>Similar Products</h2>
    {table_header}
    """
    for product in product_list[1:]:
        similar_products += get_row_html(product)
    similar_products += '</table>'
    return input_product+similar_products


recs_dict = get_recs_dict()
def display_similar_products(model=recs_dict):
    product = np.random.choice(list(model.keys()))
    st.write(get_html(model[product]), unsafe_allow_html=True)


st.write("<div class=h1>Welcome to FarmKart's Demo!</div>", unsafe_allow_html=True)
st.write("<div class=h4>Including 152 Fertilizers, 196 Pesticides, 106 Machinery, and 46 Tools & Electronics products.</h4>", unsafe_allow_html=True)
cols = st.columns([2,1,2])
with cols[1]:
    clicked = st.button('Show Similar Products')
if clicked:
    display_similar_products()
