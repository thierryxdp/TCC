def insere(lista_numeros,n):
    '''Função que dada uma lista ordenada de numeros inteiros
    e um numero n, retorne uma função onde o n seja incluso de
    maneira ordenada.list, int--> list.'''
    list.sort([n]+ lista_numeros)
    return lista_numeros.sort(lista_numeros) + [n]