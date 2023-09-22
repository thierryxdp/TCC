def insere(lista_numero,n):
    ''' funcao que dada uma lista ordenada (crescente) de numeros inteiros e um numero
        inteiro n, inclua n na posicao correta, ou seja, de modo que a lista continue ordenada
        list,int->list'''
    solucao1 = list.extend(lista_numero,[n])
    solucao2 =list.sort(solucao1)
    return lista_numero