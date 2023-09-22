def insere(lista_numero, n):
    '''função que recbe uma lista ordenada de numeros inteiros
    e um numero inteiro(n), e inclui o numero dentro da lista à mantendo 
    em ordem crescente. list, int -> list'''
    lista = list(lista_numero)
    lista.append(n)
    list.sort(lista)
    return lista