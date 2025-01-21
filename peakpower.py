import matplotlib.pyplot as plt

# 한글 폰트 설정 (Windows에서는 'Malgun Gothic', Mac에서는 'AppleGothic')
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows 사용자라면 이대로 사용

# 시간대별 전력 소비량 데이터
time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
power_consumption = [750.0016, 701.9974, 669.4183, 648.7297, 641.663, 651.5856, 683.4719, 744.1326, 
                     818.9973, 881.2446, 915.919, 928.4063, 932.8056, 949.8863, 955.4489, 961.8231, 
                     980.6668, 1004.865, 1010.165, 1011.666, 983.5811, 929.6701, 872.947, 814.7431]

# 출력 제한량 및 전기차 활용 완화량
categories = ['현재 출력 제한량 (GWh)', '전기차 활용 완화량 (GWh)']
values = [878, 95]

# 전기차 등록 대수와 출력 제한 완화량 데이터
vehicle_count = [43400, 86800, 130200]  # 전기차 등록 대수
reduction = [95, 190, 285]  # 출력 제한 완화량 (GWh)

# 시간대별 전력 소비량 그래프
plt.figure(figsize=(10, 6))
plt.plot(time, power_consumption, marker='o', label='전력 소비량 (MWh)')
plt.title('시간대별 전력 소비량 변화')
plt.xlabel('시간')
plt.ylabel('전력 소비량 (MWh)')
plt.xticks(range(1, 25))  # 1~24시로 x축 표시
plt.grid(True)
plt.legend()
plt.show()

# 출력 제한량과 전기차 활용 완화량 비교 막대그래프
plt.figure(figsize=(8, 6))
plt.bar(categories, values, color=['blue', 'green'])
plt.title('출력 제한량 vs 전기차 활용 완화량')
plt.ylabel('에너지량 (GWh)')
plt.show()

# 전기차 등록 대수와 출력 제한 완화량 관계 그래프
plt.figure(figsize=(10, 6))
plt.plot(vehicle_count, reduction, marker='o', linestyle='-', color='orange')
plt.title('전기차 등록 대수와 출력 제한 완화량 관계')
plt.xlabel('전기차 등록 대수')
plt.ylabel('출력 제한 완화량 (GWh)')
plt.grid(True)
plt.show()
