import streamlit as st
import json
from pathlib import Path

from models.highlow import draw_cards, judge

json_path = Path(__file__).parent.parent / "sample_data" / "highlow.json"

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

base_card = data["base_card"]
result_card = data["result_card"]

st.title("High and Low Game!")

if "base_card" not in st.session_state:
    st.session_state.base_card, st.session_state.result_card = draw_cards()

base_card = st.session_state.base_card
result_card = st.session_state.result_card

st.write("次のカードは大きい？ 小さい？")

st.write("最初のカード")
st.header(
    f"{base_card['suit']} {base_card['rank']}"
)

# st.write("次のカード")
# st.header(
#     f"{result_card['suit']} {result_card['rank']}"
# )

# st.button("High") 

# まだ選択していない場合
if "choice" not in st.session_state:

    st.write("次のカードを予想してください")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("High", use_container_width=True):
            st.session_state.choice = "High"
            st.rerun()

    with col2:
        if st.button("Low", use_container_width=True):
            st.session_state.choice = "Low"
            st.rerun()

# 選択した後
else:

    # 次のカードを表示
    st.write("次のカード")
    st.header(
        f"{result_card['suit']} {result_card['rank']}"
    )

    # 勝敗判定
    result = judge(
        base_card["rank"],
        result_card["rank"],
        st.session_state.choice
    )

    # 判定結果を表示
    if result == "win":
        st.success("正解！ You Win!")

    elif result == "lose":
        st.error("残念！ You Lose!")

    elif result == "draw":
        st.info("引き分け！ Draw!")

    # リセット
    if st.button("もう一度"):
        del st.session_state.choice
        del st.session_state.base_card
        del st.session_state.result_card
        st.rerun()

