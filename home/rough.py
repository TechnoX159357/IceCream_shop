def main():
    count=0
    d=dict()
    n=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    
    for i in range(n):
        k=l1[i]
        d[k]=[]
        for j in range(len(l2)):
            
            if l2[j]<k:
                d[k].append(l2[j])
        
        if d[k]==[]:
            break
        else:
            t=max(d[k])
            if t in l2:
                l2.remove(t)
                count+=1
        
    print(count+1)
main()