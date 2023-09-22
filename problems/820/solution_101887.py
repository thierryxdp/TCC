def posLetra(s, l, n):
    if s.count(l) < n:
        return -1
    if s.count(l) == n:
        return s.rindex(l)
    if n < s.count(l):
        while n < s.count(l):
            s.replace(s.rindex(l), '')
        return s.rindex(l)