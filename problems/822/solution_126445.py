def repetidos(l):
    repeticoes = 0
    for k in range (0,len(l)-1):
        if (l[k] == l[k+1]):
            repeticoes = repeticoes + 1
    return repeticoes