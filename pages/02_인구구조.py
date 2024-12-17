import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
@st.cache_data
def load_data():
    file_path = "age2411.csv"  # 파일명에 맞게 조정
    df = pd.read_csv(file_path)
    return df

# 데이터 전처리
def preprocess_data(df):
    df = df.rename(columns=lambda x: x.strip())  # 컬럼명 공백 제거
    return df

# 인구 구조 시각화 함수
def plot_population_structure(data, region):
    region_data = data[data['행정구역'].str.contains(region)]
    if region_data.empty:
        st.error("해당 지역의 데이터를 찾을 수 없습니다. 다른 지역을 입력해주세요.")
        return

    # 연령대별 인구만 추출
    age_columns = [col for col in data.columns if '세' in col]
    population = region_data[age_columns].iloc[0]

    # 그래프 생성
    plt.figure(figsize=(10, 6))
    plt.bar(age_columns, population)
    plt.xticks(rotation=90)
    plt.xlabel("연령대")
    plt.ylabel("인구 수")
    plt.title(f"{region}의 인구 구조")
    st.pyplot(plt)

# Streamlit 앱
def main():
    st.title("📊 지역별 인구 구조 분석기")
    st.write("원하는 지역을 입력하면 인구 구조를 그래프로 보여줍니다!")

    # 데이터 불러오기
    data = load_data()
    data = preprocess_data(data)

    # 사용자 입력
    region = st.text_input("🔍 지역명을 입력하세요 (예: 서울특별시 종로구)").strip()

    if st.button("인구 구조 분석"):
        if region:
            st.info(f"'{region}'의 인구 구조를 분석합니다...")
            plot_population_structure(data, region)
        else:
            st.warning("지역명을 입력해주세요.")

    # 프로젝트 주제 추천
    st.subheader("🎯 프로젝트 주제 추천")
    st.write("""
    **초등학교 5학년 대상 프로젝트 주제 아이디어**:
    - **우리 동네 인구 구조 알아보기**: 학생들이 직접 거주하는 지역의 인구 구조를 분석하고 시각화해보세요!
    - **연령대별 인구 비교**: 다른 지역과의 인구 구조를 비교하여 차이를 분석하고 발표합니다.
    - **인구 변화 예측하기**: 데이터에서 보이는 경향을 바탕으로 미래의 인구 변화를 예측해보세요.
    - **인구 구조와 지역 특성**: 인구 구조가 지역 시설(학교, 병원 등)과 어떤 관계가 있는지 조사합니다.
    """)

if __name__ == "__main__":
    main()
