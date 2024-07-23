N = int(input())
num_list = list(map(int, input().split()))
unique_list = sorted(list(set(num_list)))

# 각 값의 인덱스를 저장하는 딕셔너리를 생성합니다.
index_dict = {value: index for index, value in enumerate(unique_list)}

# 각 값을 출력합니다.
for i in range(N):
    print(index_dict[num_list[i]], end=" ")