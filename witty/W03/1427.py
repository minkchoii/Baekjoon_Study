N=input()
arr=list((map(str, N)))
arr.sort(reverse=True)
for i in range(1,len(arr)):
    arr[0]+=arr[i]
print(int(arr[0]))