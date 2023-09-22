def insere (lista_numeros,n):
    '''funcao que dada uma lista ordenada inclua n na posicao correta'''
    lista_numeros=list.sort(lista,n)
    return lista_numeros