def insere(lista_numero,n):
    '''A função recebe uma lista ordenada (crescente) de números inteiros e um número
    inteiro n e retorna outra lista, também ordenada (crescente), com a adição do número
    n na posição correta
    Parâmetros de entrada: list, int
    Valor de retorno: list'''
    #Adicionando o número n à lista
    novalista=lista_numero+[n]
    #Ordenando, de forma crescente, a nova lista
    list.sort(novalista)
    return novalista