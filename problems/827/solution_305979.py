def qtd_divisores(n):
    lista = []
    for i in range(n+1):
        if n%2==0:
            lista.append(i)
    return lista