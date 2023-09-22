def repetidos(l):
    ''''''
    elementos = 0
    x = 1
    y = 0
    while y< len(l)-1:
        if l[x] == l[y]:
            x = x + 1
            y = y + 1
            elementos = elementos + 1
    return elementos