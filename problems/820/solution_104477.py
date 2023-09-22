def posLetra(s, l, n):
    if s.count(l) <= n:
        i = 0
    	while n > 0:
            if s[i] == l:
                n -= i
            i += 1
        return i
    return -1