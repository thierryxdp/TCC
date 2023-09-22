def insere(lista_numero,n):
    '''Dado um lista ordenada de números inteirios crescentes e um número inteiro n, retorna uma nova lista crescente com n contida nela
    list,int->list'''
    
    inserido=list.append(lista_numero,n)
    ordenado=list.sort(lista_numero)
    
    return lista_numero