# -*- coding: cp949-*-   # ���� ���ڵ� ������ ���� ù�Ӹ��� ������־� ���ڵ� ������ ������

import re
import csv


# ������ ���� ���ڿ� ������ (�� �ٿ� ��� ������ ����)
playlist_title = 'spring_playlist_1'
data = "0:01 maye - Yours  3:42 �̼Ҷ��� ûȥ 7:26 Eloise : You, Dear 10:33 �鿹���� ��å"

# �� Ʈ���� �����ϱ� ���� ���� ǥ���� ���� ���� (�ð� ������ �������� ����)
split_pattern = re.compile(r'(\d+:\d+)')

# ���� ǥ������ ����Ͽ� �����͸� �ð� ������ �������� ����
tracks = split_pattern.split(data)[1:]  # ù ��° ���� ����� �� ���ڿ��̹Ƿ� ����

# ���ҵ� Ʈ�� �����͸� ó���ϱ� ���� ���ο� ����Ʈ
csv_data = []

# ���ҵ� Ʈ�� ������ ó��
for i in range(0, len(tracks), 2):
    time = tracks[i].strip()
    rest = tracks[i + 1].strip()
    artist_title = re.split(r'\s-\s|\s:', rest, 1)  # ��Ƽ��Ʈ�� ��� �и�

    if len(artist_title) == 2:
        artist, title = artist_title
    else:
        # ��Ƽ��Ʈ�� ����� ��Ȯ�� �и��� �� ���� ���('�̼Ҷ��� ûȥ'), '��'�� �������� 
        artist_title = re.split(r'\s-\s|\s:|��\s', rest, 1)
        artist, title = artist_title

    csv_data.append([time, artist, title])

# ������ CSV ���� ���
csv_file_path_updated = fr'C:\Users\user1\Project\song_recommendation_algorithm\playlists\{playlist_title}_tracks.csv'

# ������ �����ͷ� CSV ���� ����


try:
    with open(csv_file_path_updated, 'w', newline='', encoding='utf-8') as csvfile:
     writer = csv.writer(csvfile)
     writer.writerow(['Time', 'Artist', 'Title'])  # �÷� ��� �߰�
     writer.writerows(csv_data)  # ������ �ۼ�
     print('csv���� ���� �Ϸ�')

except:
    print('csv ���� ���� �� ���� �߻�')

csv_file_path_updated