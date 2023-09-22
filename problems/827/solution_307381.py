def qtd_divisores(numero):
    ''''''
    divisores=[]
    for x in range(1,numero+1):
        if numero%x==0:
            list.append(divisores,x)
    return len(divisores)