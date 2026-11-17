
import streamlit as st
import random
import json
from pathlib import Path

st.title("クイズアプリにようこそ！")
st.write("すべての問題に回答して、最後に採点ボタンを押してください。")

# JSONファイルを読み込む
json_path = Path(__file__).parent.parent / "sample_data" / "questions.json"

with open(json_path, "r", encoding="utf-8") as f:
    questions = json.load(f)

# 出題する問題数
QUESTION_COUNT = 5

# 最初にランダムで問題を選ぶ
if "selected_numbers" not in st.session_state:
    st.session_state.selected_numbers = random.sample(
        list(questions.keys()),
        min(QUESTION_COUNT, len(questions))
    )

# 採点済みかどうかを記録
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# 問題を表示
for index, number in enumerate(st.session_state.selected_numbers):

    q = questions[number]

    st.subheader(f"第{index + 1}問")
    st.write(q["問題"])

    st.radio(
        "答えを選んでください",
        options=[1, 2, 3, 4],
        format_func=lambda x, choices=q["選択肢"]: f"{x}. {choices[str(x)]}",
        index=None,
        key=f"answer_{number}",
        disabled=st.session_state.submitted
    )

    st.divider()

# 採点ボタン
if not st.session_state.submitted:

    if st.button("採点する"):

        unanswered = [
            number for number in st.session_state.selected_numbers
            if st.session_state.get(f"answer_{number}") is None
        ]

        if unanswered:
            st.warning("すべての問題に回答してください。")

        else:
            score = 0

            for number in st.session_state.selected_numbers:

                q = questions[number]

                if st.session_state[f"answer_{number}"] == q["正解"]:
                    score += 1

            st.session_state.score = score
            st.session_state.submitted = True
            st.rerun()

# 採点結果
if st.session_state.submitted:

    st.subheader("採点結果")

    st.write(
        f"あなたの得点は {st.session_state.score} / "
        f"{len(st.session_state.selected_numbers)} 問です！"
    )

    for index, number in enumerate(st.session_state.selected_numbers):

        q = questions[number]
        answer = st.session_state[f"answer_{number}"]

        if answer == q["正解"]:
            st.success(f"第{index + 1}問：正解！")
        else:
            st.error(f"第{index + 1}問：不正解")

        st.write(
            f"正解は {q['正解']}番の {q['選択肢'][str(q['正解'])]} です。"
        )
