import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows 사용자
# Mac 사용자라면 'AppleGothic' 사용 가능

# 데이터: 출력 제한량과 전기차 활용 완화량
categories = ['현재 출력 제한량 (GWh)', '전기차 활용 완화량 적용 후 (GWh)']
current_restriction = 878  # 현재 출력 제한량
ev_reduction = 95  # 전기차 활용 완화량

# 그래프 데이터
values = [current_restriction, current_restriction - ev_reduction]

# 그래프 생성
plt.figure(figsize=(10, 6))
bars = plt.bar(categories, values, color=['blue', 'green'], alpha=0.7)

# 값 표시
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 10, f"{yval:.0f} GWh", ha='center', va='bottom', fontsize=12)

# 그래프 설정
plt.title('전기차 활용을 통한 출력 제한 완화 효과', fontsize=13)
plt.ylabel('출력 제한량 (GWh)', fontsize=12)
plt.ylim(0, 1000)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 결과 출력
plt.show()
