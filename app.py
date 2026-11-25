import streamlit as st

st.set_page_config(page_title="광고 효과 계산기", page_icon="📊")

st.title("📊 광고 효과 계산기")
st.write("상품을 선택하고 광고 전후 판매량을 입력하여 광고 효과를 확인해 보세요!")

# 상품 데이터
products = {
    "텀블러": 5000,
    "책가방": 10000
}

# 상품 선택
name = st.selectbox("상품명 선택", ["텀블러", "책가방"])

# 슬라이더
investment = st.slider("투자 금액 (만원)", 100, 1000, 300, step=100)
before = st.slider("광고 전 판매량 (개)", 100, 10000, 2000, step=100)
after = st.slider("광고 후 판매량 (개)", 100, 10000, 4000, step=100)

# 광고 효과 계산 함수
def check_effect(name, before, after):
    increase = (after - before) / before
    score = int(max(0, min(80, increase * 80)))

    if after >= 4000:
        score += 20

    if score >= 70:
        effect = "상"
    elif score >= 40:
        effect = "중"
    else:
        effect = "하"

    return score, effect

# 분석하기 버튼
if st.button("📊 분석하기"):

    score, effect = check_effect(name, before, after)

    unit_profit = products[name]
    profit = (after - before) * unit_profit - investment * 10000

    if profit > 0:
        decision = "가능"
        reason = "추가 판매 이익이 광고 투자 금액보다 큽니다."
    else:
        decision = "불가능"
        reason = "추가 판매 이익이 광고 투자 금액보다 적습니다."

    st.subheader("📈 광고 효과 분석 결과")

    st.metric("광고 효과 점수", str(score) + "점", effect)

    result = {
        "상품명": name,
        "광고 효과": effect,
        "예상 이윤": f"{profit:,}원",
        "광고 지속 가능 여부": decision,
        "판단 이유": reason
    }

    table_data = []

    for key, value in result.items():
        table_data.append({
            "항목": key,
            "결과": value
        })

    st.table(table_data)

    if profit > 0:
        st.success("광고를 지속해도 이윤이 있습니다.")
    else:
        st.warning("광고를 지속하면 이윤이 발생하지 않습니다.")
