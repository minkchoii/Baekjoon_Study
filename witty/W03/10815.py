N=int(input())
sang=list(map(int, input().split()))
M=int(input())
card=list(map(int, input().split()))
index_dict = {value: index for index, value in enumerate(sang)}
for i in range(M):
    if card[i] in index_dict:
        print(1, end=" ")
    else:
        print(0, end=" ")