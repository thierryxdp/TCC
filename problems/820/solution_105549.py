def posLetra(s, l, n):
    a=0
    for i in range(len(s)):
        if s{i}==l:
            a=a+1
        if a==n:
            return i
    return -1