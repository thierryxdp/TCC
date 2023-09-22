def insere(lista_numero, n):
    '''Insere o numero inteiro n e retorna uma nova lista, porem respeitando a ordem crescente dos numeros
       parameters:
       n:numero inteiro qualquer
       lista_numero:Uma lista qualquer
       list, int->list'''
    lista_numero.append(n)
    lista_numero.sort() 
    return lista_numero