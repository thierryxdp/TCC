def insere(lista_numero, n):
    '''função que dada uma lista ordenada (crescente) de números inteiros, insere o número inteiro n na posição e ordem
    correta.
    list, int -> list'''
    
    lista_numero[1:1]=[n]
    lista = list.sort(lista_numero)
    
    return lista