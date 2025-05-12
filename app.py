import streamlit as st
import streamlit_authenticator as stauth


st.title('Login version, test')

config = {
    'credentials': {
        'usernames': {
            'yhkal': {
                'email': '1', 
                'name': 'Yehor Kalchenko',
                'password': '1'
            }
        }
    }
}

authenticator = stauth.Authenticate(
    config['credentials'],
    'cookie_name',         # будь-яка назва
    'signature_key',       # будь-який секретний ключ
    cookie_expiry_days=30  # опціонально
)

try:
    authenticator.login()
except Exception as e:
    st.error(e)

if st.session_state.get('authentication_status'):
    authenticator.logout()
    st.write(f'Welcome *{st.session_state.get("name")}*')
    st.title('Some content')
elif st.session_state.get('authentication_status') is False:
    st.error('Username/password is incorrect')
elif st.session_state.get('authentication_status') is None:
    st.warning('Please enter your username and password')