def insere(lista_numero, n):
    '''Função que recebe uma lista ordenada(crescente) e um int(n);
inclui n na posição correta fazendo a lista permanecer ordenada.
list, int-> list'''
    lista_numero.append(n)
    lista_numero.sort( )
    return lista_numero