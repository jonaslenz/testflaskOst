import streamlit as st
import subprocess
import requests
import socket
import flask

st.write("check server status")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('127.0.0.1',5000))
if result == 0:
   status_flask = True
else:
    status_flask = False
sock.close()


stop_flask = False
start_flask = False
st.button("Refresh Server Status")

if not status_flask:
    st.write("Server is down.")
    start_flask = st.button("Start the server")

    if start_flask:
        st.session_state.a = subprocess.Popen(["python", "hello1.py"], start_new_session = True, stdout = None, stdin=None, stderr= None, env=my_env)

else:
    st.write("Server is up.")

    stop_flask = st.button("Stop the server")
    r = requests.get('http://127.0.0.1:5000')
    st.write(r)
    if stop_flask:
        st.session_state.a.terminate()
        st.write("Flask stopped")
