def insere(lista_numero,n):
    ''' Funcao que dada uma lista e um numero ela coloque na posicao
    	correta de forma crescente'''
    lista_numero.append(n)
    return lista_numero.sort()