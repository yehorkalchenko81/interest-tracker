import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

if 'show_main_title' not in st.session_state:
    st.session_state.show_main_title = True

if st.session_state.show_main_title:
    st.title('Login version, test')

def login():
    try:
        authenticator.login()
    except Exception as e:
        st.error(e)

if st.session_state.get('authentication_status'):
    if st.button('Logout'):
        st.session_state['authentication_status'] = None
        st.session_state.show_main_title = True
    st.session_state.show_main_title = False
    st.write(f'Welcome *{st.session_state.get("name")}*')
    st.title('Some content')
elif st.session_state.get('authentication_status') is False:
    st.error('Username/password is incorrect')
    login()
elif st.session_state.get('authentication_status') is None:
    st.warning('Please enter your username and password')
    login()
