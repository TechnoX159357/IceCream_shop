# now we are usin bottom apporoach for fibbonacci 
def fib_bottom_up(n):
    if n==1 or n==2:
        return 1
    bottom_up=[None]*(n+1)
    bottom_up[1]=1
    bottom_up[2]=2
    for i in range(3,n+1):
        bottom_up[i]=bottom_up[i-1]+bottom_up[i-2]
    return bottom_up[n]

print(fib_bottom_up(100))
print(fib_bottom_up(10000))

# thank you