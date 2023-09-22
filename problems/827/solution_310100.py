def qtd_divisores(numero):
    lista = []
    for i in numero:
        if numero%i==0:
            lista += [i,]
    return len(lista)