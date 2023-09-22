def faltante (lista):
    '''Dado uma lista, a função deve retornar o número inteiro
    que pertence a o intervalo da lista, mas que não pertence
    a lista;
    lista -> int'''
    list.sort(lista)
    i=0
    n= len(lista)
    z=1
    while(i>n):
        if (lista[z]==lista[i]+1):
            i=i+1
            z=z+1
        else:
            return (lista[i]+1)
        
    return (lista[z]+1)