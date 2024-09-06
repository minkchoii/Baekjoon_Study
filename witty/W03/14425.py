N, M = map(int, input().split())
S = set()  # 집합으로 선언하여 중복을 자동으로 제거
Check = []

for _ in range(N):
    S.add(input())  # 집합에 문자열 추가

for _ in range(M):
    Check.append(input())

cnt = 0
for i in range(M):
    if Check[i] in S:  # Check 리스트의 각 문자열이 S 집합에 있는지 확인
        cnt += 1

print(cnt)
