def posLetra(s, l n):
    pos = []
    i = 0
    while i<len(s) and i != (-1):
        if  == str.find(s, l, i):
            pos.append(str.find (s, l, i))
            i = i + 1
            else:
                i = str.find(s, l, i)
    if (n-1) in list(range(len(pos))):
        r = pos[n-1]
    else:
        r = -1
        return r