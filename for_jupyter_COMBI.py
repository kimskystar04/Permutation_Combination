import pandas as pd
from itertools import combinations

n, r = map(int, input("Combination의 모든 경우를 출력해줄 것입니다. 전체 갯수인 n과 선택할 갯수인 r을 공백을 두고 입력하세요 by 김민규-평촌고").split())

# 전체 갯수가 n개면 자동으로 내용물은 1~n으로 한다.
per_contents = []
for i in range(1, n + 1):
    per_contents.append(i)

col = []

for i in range(r):
    col.append("원소" + str(i + 1))

ind = []
contents = []

# 본 연산 부분
for i in combinations(per_contents, r):
    contents.append(i)

for i in range(1, len(contents) + 1):
    ind.append(i)

pd.DataFrame(contents, columns=col, index=ind)