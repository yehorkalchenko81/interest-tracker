import streamlit as st
import streamlit_authenticator as stauth


st.title('Login version, test')

config = {
    'credentials': {
        'usersnames': {
            'yhkal': {
                'email': '1', 
                'name': 'Yehor Kalchenko',
                'password': stauth.Hasher(['1']).generate()[0]
            }
        }
    }
}

authenticator = stauth.Authenticate(
    config['users']
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