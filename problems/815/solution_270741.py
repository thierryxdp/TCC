def insere(lista_numero,n):
    '''dada uma lista ordenada(crescente) de num inteiros e um numero int n, inclue n na posicao correta
   fazendo com que a lista continua ordenada
    lista, int -> lista'''
    lista_numero.append(n)
    lista_numero.sort() 
    return lista_numero