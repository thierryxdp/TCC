def qtd_divisores(numero):
    x = 1
    lista = []
    quantidade = 0

    for x in range(1,numero+1):
        if numero%x == 0:
            lista.append(x)
        quantidade = len(lista)
        
    return quantidade