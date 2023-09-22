def insere(lista_numero,n):
    ''' funcao que dada uma lista ordenada (crescente) de numeros inteiros e um numero
        inteiro n, inclua n na posicao correta, ou seja, de modo que a lista continue ordenada
        list,int->list'''
    solucao= lista_numero+ [n]
    return list.sort(lista_numero)