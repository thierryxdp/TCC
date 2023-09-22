def faltante (lista):
    '''Dado uma lista, a função deve retornar o número inteiro
    que pertence a o intervalo da lista, mas que não pertence
    a lista;
    lista -> int'''
    list.sort(lista)
    i=0
    z=1
    n= len(lista)
    p= n-1
    d=0
    while(i<n):
        d= (lista[i])+1)
        if (lista[z]==d):
            i=i+1
            z=z+1
        else:
            return (lista[i]+1)
        
    return (lista[p])