# [Do it! 실습 3C-2] seq_search() 함수를 사용하여 특정 인덱스 검색하기

from    import seq_search

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{t}에서 7의 인덱스는 {seq_search(t, 7)}입니다.')
print(f'{s}에서 "n"의 인덱스는 {seq_search(s, "n")}입니다.')
print(f'{a}에서 "DTS"의 인덱스는 {seq_search(a, "DTS")}입니다.')