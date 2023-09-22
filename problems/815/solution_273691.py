def insere(lista_numero, n):
    '''Dada uma lista ordenada de numeros inteiros e um numero inteiro 'n', 
    retorna uma lista ordenada contendo o 'n';
    list, int -> list'''
    lista = lista_numero + [n]
    list.sort(lista)
    return lista