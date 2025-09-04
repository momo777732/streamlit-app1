import streamlit as st

st.set_page_config(page_title="나의 첫 배포 앱", page_icon="🎉", layout="centered")

st.title("🎉 나의 첫 Streamlit 배포 앱")
st.caption("Github -> Streamlit Cloud 배포")

name = st.text_input("이름을 입력하세요")
food = st.selectbox("좋아하는 음식은?", ["김밥", "라면", "떡볶이", "치킨", "피자"])

agree = st.checkbox("개인정보 안내를 읽고 동의합니다.")

st.divider()

if st.button("소개하기"):
    if not name:
        st.warning("이름을 입력해 주세요.")
    elif not agree:
        st.error("동의가 필요합니다.")
    else:
        st.success(f"안녕하세요. 제 이름은 {name}이고요. 저는 {food}를 좋아 합니다.")

st.write("---")
st.caption("배포 실습/Streamlit Cloud")