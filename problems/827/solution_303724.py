def qtd_divisores(numero):
    quantidade = 0
    for x in list(range(numero+1)):
        if numero%x==0:
            quantidade += 1
        return quantidade