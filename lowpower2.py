import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows 사용자 (Mac은 'AppleGothic')

# 데이터 설정
total_ev = 43400  # 현재 제주도 전기차 대수
daily_consumption_per_ev = 6  # 전기차 한 대당 하루 충전량 (kWh)
days_per_year = 365  # 1년 일수

# 전기차 보급률과 이에 따른 전기차 대수
ev_rates = [25, 50, 75, 100]  # 보급률 (%)
ev_counts = [total_ev * rate / 100 for rate in ev_rates]  # 보급률에 따른 전기차 대수

# 각 보급률에 따른 연간 완화량 계산 (GWh)
annual_reduction = [round((ev_count * daily_consumption_per_ev * days_per_year) / 1000000, 1) for ev_count in ev_counts]

# 막대 그래프 생성
plt.figure(figsize=(10, 6))
bars = plt.bar(ev_rates, annual_reduction, color='skyblue', alpha=0.8)

# 값 표시
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 2, f"{yval:.1f} GWh", ha='center', fontsize=10)

# 그래프 설정
plt.title('전기차 보급률에 따른 출력 제한 완화 효과', fontsize=16)
plt.xlabel('전기차 보급률 (%)', fontsize=12)
plt.ylabel('출력 제한 완화량 (GWh)', fontsize=12)
plt.xticks(ev_rates)  # 보급률을 x축에 표시
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 결과 출력
plt.show()
###