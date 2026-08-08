import streamlit as st

st.title("超偏見血液型診断")
st.write("※この診断で出力された結果はすべて事実無根です")
st.write("以下の項目で当てはまったものにチェックを付けてください")
st.write("---------------------------------------------")
if "a" not in st.session_state:
    st.session_state.a=0

def add_a():
    if st.session_state.a:
        st.session_state.a += 10
    else:
        st.session_state.a -= 10

st.checkbox(
    "部屋は片付いているほうだ",
    key="check",
    on_change=add_a
)

st.write(f"{st.session_state.a}")