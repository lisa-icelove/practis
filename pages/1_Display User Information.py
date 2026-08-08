import streamlit as st

st.title("ユーザー情報表示")

if "name" in st.session_state and st.session_state.name:
    st.write(f"ー名前：{st.session_state.name}")
else:
    st.error("名前が設定されていません")
    st.write("メインページで名前を入力してください")

st.write("---------------------------------------------")

if "old" in st.session_state and st.session_state.old:
    st.write(f"ー学年：{st.session_state.old}")
else:
    st.error("学年が設定されていません")
    st.write("メインページで学年を選んでください")

st.write("---------------------------------------------")

if "syumi" in st.session_state and st.session_state.syumi:
    st.write(f"ー趣味：{st.session_state.syumi}")
else:
    st.error("趣味が設定されていません")
    st.write("メインページで趣味を選んでください")

st.write("---------------------------------------------")

if "takenoko"in st.session_state and st.session_state.takenoko and st.session_state.takenoko=="たけのこ派":
    st.write(f"ー派閥：{st.session_state.takenoko}")
else:
    st.error("派閥が設定されていないか、きのこ派にされています")
    st.write("メインページでたけのこ派を選んでください")