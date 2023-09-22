def qtd_divisores(numero):
    lista=[numero]
    for i in range(1,numero):
        if numero%i==0:
            list.append(lista,i)
    return len(lista)