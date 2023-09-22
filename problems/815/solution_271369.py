def insere(lista_numero, n):
    '''Dada uma lista ordenada de números inteiros
       e um número inteiro n, inclue n na posição correta;
       list, int -> list'''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero