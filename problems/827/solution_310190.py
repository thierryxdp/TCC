def qtd_divisores(numero):
    ''' Essa função procura a quantidade de divisores que um número tem; int->int'''
    lista=[]
    for i in range(numero):
        if numero % i==0:
            lista.append(i)
    return len(lista)