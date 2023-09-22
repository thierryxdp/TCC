def insere (lista_numero, n):
    '''funcao que inclua n na posicao correta e lista continue ordenada'''
    lista_numero = (lista_numero, n)
    list.sort(lista_numero)