def qtd_divsores(numero):
    quantidade = 0
    for i in numero:
        if numero%i==0:
            quantidade +=1
    return quantidade