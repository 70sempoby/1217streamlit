import streamlit as st

# MBTI에 따른 직업과 사람 추천 데이터
mbti_data = {
    "INTJ": {
        "career": "전략가, 데이터 사이언티스트 📊, 연구원 🔬",
        "match": "논리적이고 깊이 있는 대화를 좋아하는 사람 🧠",
        "emoji": "🧙‍♂️ 마스터마인드"
    },
    "INTP": {
        "career": "철학자, 소프트웨어 개발자 💻, 이론 물리학자 🧪",
        "match": "창의적이고 열린 사고를 가진 사람 🌟",
        "emoji": "🧩 문제 해결사"
    },
    "ENTJ": {
        "career": "리더십이 필요한 CEO 👩‍💼, 프로젝트 매니저 📈, 변호사 ⚖️",
        "match": "목표 지향적이고 의지가 강한 사람 🚀",
        "emoji": "👑 대장"
    },
    "ENTP": {
        "career": "창업가 🚀, 마케팅 전략가 📣, 혁신적인 아이디어 제공자 💡",
        "match": "유머러스하고 지적인 도전을 즐기는 사람 🎭",
        "emoji": "🤹 아이디어 뱅크"
    },
    "INFJ": {
        "career": "상담사 🫂, 작가 ✍️, 인권운동가 🕊️",
        "match": "배려심 많고 공감 능력이 뛰어난 사람 ❤️",
        "emoji": "🌈 평화주의자"
    },
    "INFP": {
        "career": "예술가 🎨, 작곡가 🎼, 심리치료사 🧘",
        "match": "진정성을 중요시하고 따뜻한 마음을 가진 사람 🌻",
        "emoji": "🎨 힐러"
    },
    "ENFJ": {
        "career": "리더십 코치 📢, 교사 📚, 사회운동가 🌍",
        "match": "사람을 격려하고 이끄는 데 열정적인 사람 🌟",
        "emoji": "🦸 사람의 힘"
    },
    "ENFP": {
        "career": "모험가 🧭, 이벤트 플래너 🎉, 콘텐츠 크리에이터 📹",
        "match": "활기차고 긍정적인 에너지를 나눌 수 있는 사람 😄",
        "emoji": "🎇 에너지 폭발"
    },
    "ISTJ": {
        "career": "회계사 🧾, 법조인 ⚖️, 관리자 🏢",
        "match": "규칙을 지키고 신뢰할 수 있는 사람 🤝",
        "emoji": "🛡️ 신뢰의 상징"
    },
    "ISFJ": {
        "career": "간호사 🏥, 교사 👩‍🏫, 사서 📚",
        "match": "따뜻하고 헌신적인 관계를 중요시하는 사람 💖",
        "emoji": "🌸 수호자"
    },
    "ESTJ": {
        "career": "경영자 🏦, 군대 장교 🎖️, 조직 관리자 🗂️",
        "match": "책임감 있고 계획을 중시하는 사람 🗓️",
        "emoji": "📋 조직의 리더"
    },
    "ESFJ": {
        "career": "사회복지사 🏠, 이벤트 코디네이터 🎊, 상담사 🧑‍⚕️",
        "match": "사람들과의 관계를 소중히 여기는 사람 👨‍👩‍👧‍👦",
        "emoji": "💐 인싸 중의 인싸"
    },
    "ISTP": {
        "career": "기술자 🔧, 자동차 정비사 🚗, 수리공 🛠️",
        "match": "실용적이고 자유로운 사고를 가진 사람 ⚙️",
        "emoji": "⚔️ 장인 정신"
    },
    "ISFP": {
        "career": "화가 🎨, 요리사 👩‍🍳, 사진작가 📸",
        "match": "감성을 공유할 수 있는 따뜻한 사람 🌷",
        "emoji": "🎶 감성 아티스트"
    },
    "ESTP": {
        "career": "영업 전문가 💼, 스포츠 코치 🏅, 리스크 관리자 ⚖️",
        "match": "도전을 즐기고 활동적인 사람 🏃",
        "emoji": "🎯 도전가"
    },
    "ESFP": {
        "career": "연예인 🎤, 행사 기획자 🎪, 여행 가이드 🌍",
        "match": "즐거움을 함께 나누고 에너지를 더해줄 사람 🌞",
        "emoji": "🎭 인생의 무대"
    }
}

# Streamlit 앱 시작
st.title("🔮 MBTI 맞춤 직업 & 궁합 추천")
st.write("당신의 MBTI 유형을 선택하면 어울리는 직업과 잘 맞는 사람 유형을 알려드려요!")

# 드롭다운 메뉴
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요 👇", list(mbti_data.keys()))

# 선택된 MBTI 결과 표시
if selected_mbti:
    st.subheader(f"**{selected_mbti} 유형 {mbti_data[selected_mbti]['emoji']}**")
    st.write(f"**어울리는 직업**: {mbti_data[selected_mbti]['career']}")
    st.write(f"**잘 맞는 사람 유형**: {mbti_data[selected_mbti]['match']}")
    st.success("당신의 MBTI를 잘 활용해 멋진 직업과 좋은 사람을 만나보세요! 🚀")

