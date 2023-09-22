def qtd_divisores(numero):
    qtd=0
    for i in range(numero+1):
        if i!=0:
            if numero%i==0:
                qtd=qtd+1
    return qtd