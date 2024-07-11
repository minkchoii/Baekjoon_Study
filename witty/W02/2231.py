N=int(input())
def calculate_sum(n):
    if n//10==0:
        return n
    else:
        return n%10+calculate_sum(n//10)
    
for i in range(1,N+1):
    sum=calculate_sum(i)+i
    if sum==N:
        print(i)
        break
    if i==N:
        print(0)