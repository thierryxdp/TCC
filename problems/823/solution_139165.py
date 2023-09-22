def faltante (lista):
    '''Dado uma lista, a função deve retornar o número inteiro
    que pertence a o intervalo da lista, mas que não pertence
    a lista;
    lista -> int'''
    list.sort(lista)
    n= len(lista)
    i=0
    lista2=[]
    
    while i<n+1:
        lista2=lista2+[i+1,]
        i=i+1
        
    return(sum(lista2)-sum(lista))