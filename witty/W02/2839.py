N=int(input())

cnt=N//5
while cnt>=0:
    left=N-cnt*5
    if left%3!=0:
        cnt-=1
        continue
    else:
        print(cnt+left//3)
        break
if cnt<0:
    print(-1)
