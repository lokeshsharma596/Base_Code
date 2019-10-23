a=int(input())
b=list(map(int,input().strip().split(' ')))
c=int(input())
d=list(map(int,input().strip().split(' ')))

l1=set(b).difference(set(d))
l2=set(d).difference(set(b))

p=sorted(l1.union(l2))

for i in p:
    print(i)
