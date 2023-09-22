def posLetra(s, l, n):
    if 0 < s.count(l) <= n:
        i = 0
    	while n > 0 and i < len(s):
            if s[i] == l:
                n -= 1
            i += 1
        return i
    return -1