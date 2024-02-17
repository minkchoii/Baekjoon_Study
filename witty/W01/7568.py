num = int(input())
x = []
y = []
grade = []
for i in range(num):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in range(num):
    cnt=0
    for j in range(num):
        if(x[i]<x[j] and y[i]<y[j]):
            cnt+=1
    grade.append(cnt+1)

for p in grade:
    print(p, end=" ")