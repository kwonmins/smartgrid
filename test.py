import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 불러오기
file_path = 'C:/Users/민성/Desktop/스마트그리드/배추값예측/venv/HOME_전력수급_최대전력수급.xlsx'
data = pd.ExcelFile(file_path)
df = data.parse('Sheet1')

# 결측치 처리
for column in ['평균기온', '평균습도', '인구']:
    df[column].fillna(df[column].mean(), inplace=True)

# 학습 데이터 확장 (시뮬레이션 데이터 추가)
simulated_populations = [60000000, 70000000, 80000000, 90000000, 100000000]  # 인구 시뮬레이션
simulated_data = pd.DataFrame({
    '평균기온': df['평균기온'].mean(),
    '인구': simulated_populations,
    '최대전력(MW)': [None] * len(simulated_populations)  # 예측 목표
})
df_extended = pd.concat([df, simulated_data], ignore_index=True)

# 피처와 타겟 변수 정의
features = df_extended[['평균기온', '인구']]
target = df_extended['최대전력(MW)']

# 학습 데이터에서 결측치 제거 (시뮬레이션 데이터는 제외)
valid_data = df[~df['최대전력(MW)'].isnull()]
X_train, X_test, y_train, y_test = train_test_split(
    valid_data[['평균기온', '인구']], valid_data['최대전력(MW)'], test_size=0.2, random_state=42
)

# 랜덤 포레스트 회귀 모델 학습
rf_model = RandomForestRegressor(n_estimators=200, max_depth=15, random_state=42)
rf_model.fit(X_train, y_train)

# 선형 회귀 모델 학습 (비교를 위해)
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# 시뮬레이션 데이터로 예측 수행
new_population_data = [60000000, 70000000, 100000000]
predicted_peak_power_rf = [rf_model.predict([[df['평균기온'].mean(), pop]])[0] for pop in new_population_data]
predicted_peak_power_lr = [lr_model.predict([[df['평균기온'].mean(), pop]])[0] for pop in new_population_data]

# 결과 출력
print("\n랜덤 포레스트 예측 결과:")
for pop, power in zip(new_population_data, predicted_peak_power_rf):
    print(f"인구: {pop:,}명 -> 예측 최대전력: {power:.2f} MW")

print("\n선형 회귀 예측 결과:")
for pop, power in zip(new_population_data, predicted_peak_power_lr):
    print(f"인구: {pop:,}명 -> 예측 최대전력: {power:.2f} MW")

# 결과 시각화
plt.figure(figsize=(10, 6))
#plt.plot(new_population_data, predicted_peak_power_rf, marker='o', label='랜덤 포레스트 예측')
plt.plot(new_population_data, predicted_peak_power_lr, marker='s', label='선형 회귀 예측', linestyle='--')
plt.title('인구 증가에 따른 예측 최대전력 (선형 회귀)')
plt.xlabel('인구')
plt.ylabel('최대전력 (MW)')
plt.grid(True)
plt.legend()
plt.show()
