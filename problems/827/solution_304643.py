def qtd_divisores(m):
    i = 0
    contador = 0
    while (i<=m):
        i = i + 1
        if (m>0)and(m%i==0):
            contador = contador + 1
    return contador