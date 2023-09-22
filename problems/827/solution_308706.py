def qtd_divisores(numero):
    quantidade = 0
    for i in range(1,numero):
        if numero%i==0:
            quantidade +=1
    return quantidade