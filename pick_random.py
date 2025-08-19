import random

# 파일에서 문자열 읽기
with open("station_names.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 줄바꿈, 공백 제거하고 모든 문자 연결
all_chars = "".join(text.split())

# 집합으로 변환해서 유니크 문자 추출
unique_chars = set(all_chars)

# 랜덤으로 한 글자 선택
if unique_chars:  # 집합이 비어있지 않은 경우
    random_char = random.choice(list(unique_chars))
    print(f"랜덤 선택된 문자: {random_char}")
else:
    print("유니크한 문자가 없습니다.")