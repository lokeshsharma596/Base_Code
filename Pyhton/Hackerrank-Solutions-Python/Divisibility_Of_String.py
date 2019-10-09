def lengthcount(s):
    patt = ''
    a, b = 0, 1
    while b < len(s):
        if s[a] == s[b]:
            a += 1
        elif a != 0:
            b -= 1
        else:
            a = 0
        b += 1
    if (b-a) != len(s) and len(s) % (b-a) == 0:
        for i in range(a, b):
            patt += s[i]
        return len(patt)


def findSmallestDivisor(s, t):
    if s==t:
        return lengthcount(s)
    elif len(s) % len(t) == 0:
        for i in range(1, int(len(s)/len(t))):
            p = s*i
            if p == s:
                return lengthcount(s)
    else:
        return -1


