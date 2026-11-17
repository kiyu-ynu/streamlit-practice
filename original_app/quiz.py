
import streamlit as st
import json
import random
from pathlib import Path

#タイトル等
st.title("クイズアプリにようこそ！")
st.write("5問のクイズに挑戦してみましょう。")

#問題データ
questions = {
    1: {
        "問題": "日本で二番目に大きい山は？",
        "選択肢": {
            1: "富士山",
            2: "桜島",
            3: "北岳",
            4: "阿蘇山"
        },
        "正解": 3
    },
    2: {
        "問題": "日本で二番目に長い川は？",
        "選択肢": {
            1: "信濃川",
            2: "利根川",
            3: "筑波川",
            4: "長良川"
        },
        "正解": 2
    },
    3: {
        "問題": "日本で二番目に人口が多い都道府県は？",
        "選択肢": {
            1: "東京都",
            2: "大阪府",
            3: "神奈川県",
            4: "愛知県"
        },
        "正解": 3
    },
    4: {
        "問題": "日本で二番目に流域面積が大きい川は？",
        "選択肢": {
            1: "信濃川",
            2: "利根川",
            3: "石狩川",
            4: "北上川"
        },
        "正解": 3
    },
    5: {
        "問題": "日本で二番目に面積の大きい都道府県は？",
        "選択肢": {
            1: "北海道",
            2: "福島県",
            3: "新潟県",
            4: "岩手県"
        },
        "正解": 4
    }
}


question_numbers = list(questions.keys())
selected_numbers = random.sample(question_numbers, 1)

st.button(1, key="question_1")
st.button(2, key="question_2")
st.button(3, key="question_3")
st.button(4, key="question_4")
