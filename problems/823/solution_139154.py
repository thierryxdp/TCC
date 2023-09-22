def faltante (lista):
    '''Dado uma lista, a função deve retornar o número inteiro
    que pertence a o intervalo da lista, mas que não pertence
    a lista;
    lista -> int'''
    list.sort(lista)
    i=0
    z=1
    n= len(lista)
    m=lista[z]
    x=lista[i]
    while(i<n):
        if(m==x+1):
            i=i+1
            z=z+1
        else:
            if(1 in  lista):
                return (lista[n]+1)
            else:
                return (1)
        
    return (lista[n]+1)