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
    },
    "코딩 스타일을 배우는 'Clean Code'": {
        "author": "Robert C. Martin",
        "summary": "가독성과 유지보수가 쉬운 코드 작성법을 배우며 좋은 개발 습관을 기를 수 있습니다.",
        "audience": "프로그램을 작성하는 능력을 한 단계 끌어올리고 싶은 학생"
    },
    "컴퓨터의 원리를 이해하는 '코드: 하드웨어와 소프트웨어의 비밀'": {
        "author": "Charles Petzold",
        "summary": "컴퓨터의 하드웨어와 소프트웨어가 어떻게 작동하는지 알기 쉽게 설명합니다.",
        "audience": "컴퓨터 시스템의 근본 원리를 배우고 싶은 학생"
    },
    "AI를 배우는 'Deep Learning with Python'": {
        "author": "François Chollet",
        "summary": "파이썬과 Keras를 사용하여 딥러닝 모델을 구현하는 방법을 배울 수 있습니다.",
        "audience": "딥러닝과 인공지능에 관심 있는 학생"
    },
    "문제 해결의 중요성 '생각하는 프로그래밍'": {
        "author": "John Bentley",
        "summary": "프로그래밍 문제를 창의적으로 해결하고 논리적 사고를 키울 수 있습니다.",
        "audience": "문제 해결 능력을 키우고 싶은 학생"
    },
    "AI 기초 '혼자 공부하는 머신러닝+딥러닝'": {
        "author": "박해선",
        "summary": "머신러닝과 딥러닝의 기초부터 실습까지 배울 수 있는 입문서입니다.",
        "audience": "인공지능 개발의 기초를 쌓고 싶은 학생"
    },
    "알고리즘 기초 'Algorithm 101'": {
        "author": "김도형",
        "summary": "알고리즘을 기초부터 차근차근 배울 수 있습니다. 문제 풀이와 실습을 포함합니다.",
        "audience": "알고리즘 공부를 시작하고 싶은 학생"
    },
    "인터넷의 역사 '인터넷의 역사'": {
        "author": "Katie Hafner",
        "summary": "인터넷의 발전 과정과 기술적 배경을 이해할 수 있습니다.",
        "audience": "인터넷과 네트워크에 대한 기초 지식을 쌓고 싶은 학생"
    },
    "알고리즘 인터뷰 대비 '파이썬 알고리즘 인터뷰'": {
        "author": "박상길",
        "summary": "파이썬을 활용해 알고리즘 문제를 풀고 코딩 인터뷰에 대비할 수 있습니다.",
        "audience": "취업 준비를 위해 알고리즘 역량을 키우고 싶은 학생"
    },
    "IT 입문서 'IT 좀 아는 사람'": {
        "author": "정지훈",
        "summary": "IT 산업과 기술을 알기 쉽게 설명하는 입문서로 IT 세계를 이해하는 첫걸음이 됩니다.",
        "audience": "IT 산업 전반에 대한 이해를 넓히고 싶은 학생"
    },
    "운영체제의 역사 '유닉스의 탄생'": {
        "author": "Brian W. Kernighan",
        "summary": "유닉스 운영체제의 탄생과 발전 과정을 통해 IT 혁신을 이해합니다.",
        "audience": "운영체제와 컴퓨터 역사에 관심 있는 학생"
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
