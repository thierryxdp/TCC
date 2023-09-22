def qtd_divisores(numero):
    '''função que determina a quantidade de divisores que um
    numero possui.
    int->int'''
    divisores=[]
    for num in range(1,len(numero+1)):
        if (numero%num)==0:
            list.append(divisores,num)
    return list.count(divisores)