def qtd_divisores(numero):
    ''' Essa função procura a quantidade de divisores que um número tem; int->int'''
    lista=[]
    for i in range(1,numero+1):
        if numero % i==0:
            lista.append(i)
    return len(lista)