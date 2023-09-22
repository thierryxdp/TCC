def qtd_divisores(n):
    lista = []
    for x in range(1,n+1):
        if n % x  == 0:
            lista.append(x)
    return len(lista)