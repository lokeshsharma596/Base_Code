N = int(input())

for i in range(0, N):
    s = input()
    print(s[0:len(s):2]+' '+s[1:len(s):2])
