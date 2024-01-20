import streamlit as st
import subprocess
import requests
import socket
import flask
import os

ports = {
    '5000': False,
    '5001': False,
    '5002': False}

def check_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1',int(port)))
    if result == 0:
        status_flask = True
    else:
        status_flask = False
    sock.close()
    return status_flask
if not 'a' in st.session_state:
    st.session_state.a=[]

for z in ports:
    st.header(z)
    ports[z] = check_port(z)
    stop_flask = False
    start_flask = False
    st.button("Refresh Server Status")

    if not ports[z]:
        st.write("Server is down.")
        start_flask = st.button("Start the server")

        if start_flask:
            st.session_state.a[z] = subprocess.Popen(["python", "hello"+z+".py"], start_new_session = True, stdout = None, stdin=None, stderr= None)

    else:
        st.write("Server is up.")
        stop_flask = st.button("Stop the server")
        r = requests.get('http://127.0.0.1:'+z)
        st.write(r)
        if stop_flask:
            st.session_state.a[z].terminate()
            st.write("Flask stopped")
