import streamlit as st

# IT계열 추천 도서 목록과 요약 정보
books = {
    "코딩의 기초부터 배우는 '혼자 공부하는 파이썬'": {
        "author": "윤인성",
        "summary": "프로그래밍이 처음인 사람도 쉽게 따라할 수 있는 파이썬 기초서입니다. 코드 예제와 실습을 통해 스스로 프로그래밍의 기본 개념을 익힐 수 있습니다.",
        "audience": "프로그래밍에 입문하고 싶은 고등학생"
    },
    "AI 시대를 이해하는 '사피엔스'": {
        "author": "유발 하라리",
        "summary": "인류의 역사와 기술 발전 과정을 다루며, 인공지능 시대의 도래와 미래에 대해 생각해볼 기회를 제공합니다.",
        "audience": "기술의 역사와 미래를 함께 고민하고 싶은 학생"
    },
    "컴퓨터 과학의 기본을 배우는 'CS50 교재'": {
        "author": "David J. Malan",
        "summary": "하버드대 인기 수업인 CS50을 기반으로 한 교재로, 컴퓨터 과학의 기초 개념을 배우고 프로그래밍 사고력을 키울 수 있습니다.",
        "audience": "컴퓨터 공학이나 소프트웨어 전공을 준비하는 학생"
    },
    "미래 IT 기술을 다룬 '클라우드 네이티브'": {
        "author": "Kelsey Hightower",
        "summary": "클라우드 기술과 Kubernetes를 중심으로 한 최신 IT 인프라 구축법을 설명합니다. IT 트렌드를 이해하고 싶은 학생에게 적합합니다.",
        "audience": "클라우드 기술에 관심 있는 IT 진로 준비생"
    },
    "데이터를 활용하는 '데이터 과학자 되는 법'": {
        "author": "Joel Grus",
        "summary": "데이터 과학자가 되기 위해 알아야 할 필수 기술과 프로세스를 소개합니다. 데이터 분석과 머신러닝에 대한 기초 지식을 배울 수 있습니다.",
        "audience": "데이터 분석 및 AI 분야를 목표로 하는 학생"
    }
}

# Streamlit 앱
def main():
    st.title("📚 IT 계열 진학을 꿈꾸는 고등학생을 위한 추천 도서")
    st.write("IT 분야를 공부하고 싶은 학생들을 위해 엄선한 추천 도서 목록과 간단한 내용을 확인해 보세요!")

    # 책 선택 드롭다운 메뉴
    book_title = st.selectbox("📖 읽고 싶은 책을 선택하세요", list(books.keys()))

    # 선택된 책 정보 표시
    if book_title:
        st.subheader(f"**{book_title}**")
        st.write(f"**저자**: {books[book_title]['author']}")
        st.write(f"**대상 독자**: {books[book_title]['audience']}")
        st.write(f"**책 내용 요약**:")
        st.info(books[book_title]['summary'])

        # 추천 마무리 메시지
        st.success("미리 준비된 지식을 쌓고 IT 전문가의 꿈을 이루세요! 🚀")

if __name__ == "__main__":
    main()
