def insere(lista_numero,n):
    '''função que dada uma lista ordenada(crescente) de númeors inteiros e um número inteiro n, inclua n na posição correta de maneira que a lista continue ordenada:
       list, int -> list'''
    f1=lista_numero
    f2=[n]
    f3=f1+f2
    list.sort(f3)
    return f3