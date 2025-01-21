import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows 사용자 (Mac은 'AppleGothic')

# 데이터 설정
total_ev = 43400  # 현재 제주도 전기차 대수
peak_power = 90  # 제주도 최대 전력 수요 (GW)
ev_to_reduction = 100000  # 전기차 10만 대당 1GW 피크 감소

# 전기차 보급률과 이에 따른 전기차 대수
ev_rates = [25, 50, 75, 100]  # 보급률 (%)
ev_counts = [total_ev * rate / 100 for rate in ev_rates]  # 보급률에 따른 전기차 대수

# 각 보급률에 따른 피크 전력 감소량 계산 (GW)
peak_reduction = [
    round(ev_count / ev_to_reduction, 2) for ev_count in ev_counts
]

# 피크 전력 감소 비율 계산 (%)
peak_reduction_rates = [
    round((reduction / peak_power) * 100, 2) for reduction in peak_reduction
]

# 그래프 생성
fig, ax1 = plt.subplots(figsize=(10, 6))

# 피크 전력 감소 비율 바 그래프
bars = ax1.bar(ev_rates, peak_reduction_rates, color='skyblue', alpha=0.8)
ax1.set_xlabel('전기차 보급률 (%)', fontsize=12)
ax1.set_ylabel('피크 전력 감소 비율 (%)', fontsize=12, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# 값 표시
for bar in bars:
    yval = bar.get_height()
    if yval >= 1.0:
        ax1.text(bar.get_x() + bar.get_width()/2, yval + 0.1, f"{yval:.2f}%", ha='center', fontsize=10, color='blue')

# 피크 전력 감소량 라인 그래프
ax2 = ax1.twinx()
ax2.plot(ev_rates, peak_reduction, color='orange', marker='o', linestyle='-', linewidth=2, markersize=6)
ax2.set_ylabel('피크 전력 감소량 (GW)', fontsize=10, color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# 값 표시
for i, txt in enumerate(peak_reduction):
    if txt >= 0.12:
        ax2.annotate(f"{txt:.2f} GW", (ev_rates[i], peak_reduction[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10, color='orange')

# 그래프 설정
plt.title('전기차 보급률에 따른 피크 전력 감소 효과', fontsize=16)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# 결과 출력
plt.show()
