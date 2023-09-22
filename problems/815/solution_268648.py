def insere(lista_numero,n):
    '''Função que dada uma lista ordenada(crescente) de números inteiros e um número inteiro n
    inclua n na posição correta'''
    lista1=list.append(lista_numero,n)
    lista2=list.sort(lista1)
    return lista2