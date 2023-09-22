def posLetra(s, l, n):
    if 0 < s.count(l) <= n:
        i = 0
        while n > 0:
            i = s.find(l, i)
            n -= 1
        return i
    return -1