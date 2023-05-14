import streamlit as st
import time
import os
from css import load_css; load_css()



if 'count' not in st.session_state:
    st.session_state['count'] = 0
def analyze():
    messages = {
        1:"""<br><br><div class="message">Will</div><br><div class="submessage">(oops, didn't work completely, keep going!)</div>""",
        2:"""<br><br><div class="message">You</div><br><div class="submessage">(GAH KEEP GOING!)</div>""",
        3:"""<br><br><div class="message">Marry</div><br><div class="submessage">(Almost there...)</div>""",
        4:"""<br><br><div class="message">Me?!</div>""",
    }
    st.session_state['count'] += 1
    with st.spinner('Understanding barks...'):
        # time.sleep(3)
        st.write(messages[st.session_state['count']], unsafe_allow_html=True)
        if st.session_state['count'] == 4:
            st.balloons()
            images = [(n, f'images/{i}') for n, i in \
                        zip([0,1,2]*100, sorted(os.listdir('images')))]
            cols = st.columns(3)
            with st.container():
                for n, image in images:
                    with cols[n]:
                        st.image(image, use_column_width=True)
    if st.session_state['count'] == 4:
        st.session_state['count'] = 0


st.write("<div class=h1>Welcome to the Bark Analyzer!</div>", unsafe_allow_html=True)
st.write("<div class=h4>For when your dog is talking at you and you want to know what it all means.</h4>", unsafe_allow_html=True)
cols = st.columns([3,1,3])
with cols[1]:
    clicked = st.button("What's my dog saying?")
if clicked:
    analyze()
