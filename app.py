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
    st.session_state.a={}

st.button("Refresh Server Status")
start_flask = {}
stop_flask = {}

for z in ports:
    st.header(z)
    ports[z] = check_port(z)
    stop_flask[z] = False
    start_flask[z] = False

    if not ports[z]:
        st.write("Server is down.")
        start_flask[z] = st.button("Start the server "+z)

        if start_flask[z]:
            st.session_state.a[z] = subprocess.Popen(["python", "hello"+z+".py"], start_new_session = True, stdout = None, stdin=None, stderr= None)

    else:
        st.write("Server is up.")
        stop_flask[z] = st.button("Stop the server "+z)
        r = requests.get('http://127.0.0.1:'+z)
        st.write(r)
        if stop_flask[z]:
            st.session_state.a[z].terminate()
            st.write("Flask stopped")
