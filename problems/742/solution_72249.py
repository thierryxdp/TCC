def substitui(s, x, i):
    n = i - 1
    p = n + 2
    parte1 = s[:i] 
    parte2 = s[p:]
    return str(parte1) + str(x) + str(parte2)