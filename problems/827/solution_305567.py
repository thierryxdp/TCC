def qtd_divisores(numero):
    '''função que retorna o numerro de divisoresde um numero,int-->int'''
    lista=[]
    for num in range (1,numero+1):
        if numero%num==0:
            lista.append(num)
            return (lista)