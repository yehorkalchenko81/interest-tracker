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

def register():
    try:
        email_of_registered_user, \
        username_of_registered_user, \
        name_of_registered_user = authenticator.register_user(
            merge_username_email=False,
            password_hint=False,
            captcha=False
        )

        if email_of_registered_user and username_of_registered_user:
            existing_usernames = config['credentials']['usernames'].keys()
            existing_emails = [config['credentials']['usernames'][u]['email'] for u in existing_usernames]

            if username_of_registered_user in existing_usernames:
                st.error('Username already exists')
            elif email_of_registered_user in existing_emails:
                st.error('Email already registered')
            else:
                st.success('User registered successfully')

    except Exception as e:
        st.error(f'Error during registration: {e}')

        
login_button = st.button('Login')
register_button = st.button('Register')

if login_button:
    login()
elif register_button:
    register()

if st.session_state.get('authentication_status'):
    st.session_state.show_main_title = False
    st.write(f'Welcome *{st.session_state.get("name")}*')

    if st.button('Logout'):
        st.session_state['authentication_status'] = None
        st.session_state.show_main_title = True

    st.title('Some content')
elif st.session_state.get('authentication_status') is False:
    st.error('Username/password is incorrect')
