def insere(lista_numero, n):
    '''função que, dada uma lista ordenada(crescente) de números inteiros e 
    um número inteiro n, inclua n na posição correta, de tal maneira que a
    lista continue ordenada.
    list,int->list'''
    lista = lista_numero.append(n)
    lista_ordenada = sort(lista)
    return lista_ordenada