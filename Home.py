import streamlit as st
from pathlib import Path

st.title("ゲームアプリへようこそ！")

st.write("このアプリでは、さまざまなゲームを楽しむことができます。")

st.write("これからも新しいゲームを追加していく予定です。")
st.write("以下のURLからゲームの種類と遊び方を確認できます。")
st.write("[ゲームの種類と遊び方](https://kiyu-ynu.github.io/streamlit-practice/)")

st.write("左側のサイドバーから遊びたいゲームを選択してください！")
image_path = Path(__file__).parent / "2026-11-20-17-32-58.png"

st.image(image_path, caption="この中からゲームを選ぶ")