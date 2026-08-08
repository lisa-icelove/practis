import streamlit as st

st.title("ユーザー情報表示")

st.write(f"-名前：{st.session_state.name}")

st.write("---------------------------------------------")

st.write(f"-学年：{st.session_state.old}")

st.write("---------------------------------------------")

st.write(f"-趣味：{st.session_state.syumi}")