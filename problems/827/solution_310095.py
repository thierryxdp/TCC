def qtd_divisores(y):
    i=0
    for x in range(y):
        if y%(x+1) ==0:
            i = i+1
    return i