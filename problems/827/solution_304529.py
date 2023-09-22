def qtd_divisores(numero):
    pos = 0
    lista_divisores = []
    for elemento in range(numero):
        if numero%(elemento+1) == 0:
            list.append(lista_divisores,numero/(elemento+1))
        pos = pos + 1
    return len(lista_divisores)