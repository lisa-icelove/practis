import streamlit as st

if st.button("ユーザー情報をすべてリセット"):
    st.session_state.name=""
    st.session_state.old=""
    st.session_state.syumi=""
    st.session_state.takenoko=""