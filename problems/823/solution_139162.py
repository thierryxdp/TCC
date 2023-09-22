def faltante (lista):
    '''Dado uma lista, a função deve retornar o número inteiro
    que pertence a o intervalo da lista, mas que não pertence
    a lista;
    lista -> int'''
    list.sort(lista)
    n= len(lista)
    m=lista[1]
    x=lista[0]
    p=lista[n-1]
    
    if (1 in  lista):
        while(0<=n):
            if(m==x+1):
                x=x+1
                m=m+1
                return (p+1)
            else:
                return x+1
    else:
        return (1)