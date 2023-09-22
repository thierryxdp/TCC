def qtd_divisores(numero):
    lista_divisores=[numero]
    for i in range(1,numero):
        if numero%i==0:
            list.append(lista_divisores,i)
    return len(lista_divisores)