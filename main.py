import streamlit as st

st.title("ユーザ情報入力")

if "name" not in st.session_state:
    st.session_state.name=""

if "old" not in st.session_state:
    st.session_state.old=""

if "syumi" not in st.session_state:
    st.session_state.syumi=""

if "takenoko" not in st.session_state:
    st.session_state.takenoko=""

name=st.text_input("名前を入力してください")
if st.button("名前を保存"):
    st.session_state.name=name

old=st.selectbox(
    "あなたの学年を選んでください",
    ["小学5年生","小学6年生","中学1年生","中学2年生","中学3年生"]
)
if st.button("学年を保存"):
    st.session_state.old=old

syumi=st.multiselect(
    "趣味を選んでください(複数選択可)",
    ["読書","スポーツ","ゲーム","音楽","絵画","その他"]
)
if st.button("趣味を保存"):
    st.session_state.syumi=", ".join(syumi)

takenoko=st.radio(
    "あなたはどちら派ですか？",
    ["たけのこ派","きのこ派"]
)
if st.button("派閥を保存"):
    st.session_state.takenoko=takenoko