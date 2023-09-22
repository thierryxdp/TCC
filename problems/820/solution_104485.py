def posLetra (s, l, n):
    o = 0
    for i in str.count(s, l):
        if s[1] == 1:
            o += 1
        if o == 0:
            return 1
    return -1