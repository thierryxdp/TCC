def qtd_divisores(numero):
    lista = 0
    for n in numero:
        if numero%n==0:
            lista = lista + n
    return lista