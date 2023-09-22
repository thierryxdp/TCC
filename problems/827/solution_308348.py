def qtd_divisores(x):
    div = 0
    for c in range (1,x+1):
        if (x%c == 0):
            div=div+1
    return div