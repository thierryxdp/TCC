def insere(lista_numero,n):
    ''' Funcao que dada uma lista e um numero ela coloque na posicao
    	correta de forma crescente'''
    lista_numero.append(n)
    lista_numero = lista_numero.sort()
    return lista_numero