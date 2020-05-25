# -*- coding: utf-8 -*-
"""
Created on Mon May 25 21:13:23 2020

@author: shinm
"""
#sqrt를 사용하기 위한 math 라이브러리 호출
from math import sqrt

# 사람에 대한 영화 선호도
critics = {
    'smc' : {'spiderman' : 5, 'edward': 4.5, 'getout': 3},
    'ljh' : {'spiderman' : 4, 'getout' : 2},
    'lhj' : {'spiderman' : 4, 'edward': 3.5, 'getout' : 1},
    'sms' : {'spiderman' : 3, 'edward': 4, 'getout' : 5}
}

# 사람 한명에 대한 딕셔너리 값 추출
print(critics.get('smc').get('spiderman'))

# 비교 함수
def similar(i, j):
    return sqrt(pow(i, 2) + pow(j, 2))

# 2명에 대한 비교
value1 = critics['smc']['spiderman'] - critics['lhj']['spiderman']
value2 = critics['smc']['edward'] - critics['lhj']['edward']

#print(similar(value1, value2))

# smc를 대상으로 다른 사람들 전체와의 spiderman, edward scissorhands 평점으로
# 거리를 구해보자

# 2명 이상과의 거리 구하기
for i in critics:
    if i != 'smc':
        val1 = critics.get('smc').get('spiderman') - critics.get(i).get('spiderman')
        val2 = critics.get('smc').get('getout') - critics.get(i).get('getout')
        print(i, ' = ', similar(val1, val2))
        # 비교를 위한 정규화(변수 재설정)
        print(i, ' = ', 1/(1 + similar(val1, val2)))