# -*- coding: cp949-*-   # 파일 인코딩 형식을 파일 첫머리에 명시해주어 인코딩 오류를 방지함

import re
import csv


# 수정된 원본 문자열 데이터 (한 줄에 모든 데이터 포함)
playlist_title = 'spring_playlist_1'
data = "0:01 maye - Yours  3:42 이소라의 청혼 7:26 Eloise : You, Dear 10:33 백예린의 산책"

# 각 트랙을 구분하기 위한 정규 표현식 패턴 정의 (시간 패턴을 기준으로 분할)
split_pattern = re.compile(r'(\d+:\d+)')

# 정규 표현식을 사용하여 데이터를 시간 패턴을 기준으로 분할
tracks = split_pattern.split(data)[1:]  # 첫 번째 분할 결과는 빈 문자열이므로 제외

# 분할된 트랙 데이터를 처리하기 위한 새로운 리스트
csv_data = []

# 분할된 트랙 데이터 처리
for i in range(0, len(tracks), 2):
    time = tracks[i].strip()
    rest = tracks[i + 1].strip()
    artist_title = re.split(r'\s-\s|\s:', rest, 1)  # 아티스트와 곡명 분리

    if len(artist_title) == 2:
        artist, title = artist_title
    else:
        # 아티스트와 곡명을 명확히 분리할 수 없는 경우('이소라의 청혼'), '의'를 기준으로 
        artist_title = re.split(r'\s-\s|\s:|의\s', rest, 1)
        artist, title = artist_title

    csv_data.append([time, artist, title])

# 수정된 CSV 파일 경로
csv_file_path_updated = fr'C:\Users\user1\Project\song_recommendation_algorithm\playlists\{playlist_title}_tracks.csv'

# 수정된 데이터로 CSV 파일 생성


try:
    with open(csv_file_path_updated, 'w', newline='', encoding='utf-8') as csvfile:
     writer = csv.writer(csvfile)
     writer.writerow(['Time', 'Artist', 'Title'])  # 컬럼 헤더 추가
     writer.writerows(csv_data)  # 데이터 작성
     print('csv파일 생성 완료')

except:
    print('csv 파일 생성 중 오류 발생')

csv_file_path_updated