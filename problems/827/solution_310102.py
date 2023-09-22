def qtd_divisores(numero):
    lista = []
    for i+1 in range(numero):
        if numero%i==0:
            lista += [i,]
    return len(lista)