def faltante(lista):
    '''função  recebe  lista  e  retorna  um numero inteiro
    que pertence ao intervalo [1, N] '''
    'list--> int'
    i=0
    
    lista1=list.sort(lista)
    lista1 = list(range(1, len(lista)+2))
    
    while  len(lista1)  >  i+1:
        
        if lista[i] != lista1[i]:
            return lista1[i]

        i +=1

    return  lista1[-1]