def qtd_divisores(n):
    i =0 
    for x in range(n):
        if x%(n+1) ==0:
            i == i+1
    return i