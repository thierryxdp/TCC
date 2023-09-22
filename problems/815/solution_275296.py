def insere(lista_numero, n):
    '''Essa funcao dada uma lista ordenada (crescente) de números inteiros e um número inteiro n, inclua n na posição correta, ou seja, de tal maneira que a lista continue ordenada;
    Recebe uma lista ordenada e um numero 
    Retorna o numero na lista ordenada.'''
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero