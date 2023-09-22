def qtd_divisores(numero):
    '''Dado um número inteiro, retorna quantos divisores
    este número possui.
    int -> int'''
    lista_divisores=[]
    for i in range(numero+1):
        if numero%i==0:
            list.append(lista_divisores,i)
    return sum(lista_divisores)