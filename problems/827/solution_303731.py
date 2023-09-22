def qtd_divisores(numero):
    cont = 0
    for x in range(1,numero+1):
        if numero%x==0:
            cont += 1
    return cont