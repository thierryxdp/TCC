def repetidos(l):
    i = 1
    r = 0
    while i < len(l):
        if l[i] == l[i - 1]:
            r += 1
    	i += 1
    return r