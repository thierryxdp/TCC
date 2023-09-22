def qtd_divisores(numero):
    quantidade = 0
    for x in range(1,numero+1):
        if numero%(x-1)==0:
            quantidade += 1
        return quantidade