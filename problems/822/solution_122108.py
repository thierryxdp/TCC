def repetidos(l):
    ''''''
    elementos = 0
    x = 0
    y = 1
    while x< len(l)-1:
        if l[x] == l[y]:
            x = x + 1
            y = y + 1
            elementos = elementos + 1
    return elementos