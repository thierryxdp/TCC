def insere(lista_numero,n):
    '''Função que dada uma lista ordenada, de maneira crescente, de números inteiros(lista_numero) e um número interiro(n), inclui n na posição correta, de forma que a lista continue ordenada.
    parâmetros de entrada:list, int
    valor de retorno:list'''
    novalista=lista_numero+[n]
    list.sort(novalista)
    return novalista