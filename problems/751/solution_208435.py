def intercala(lista1, lista2):
    """É uma função que dadas duas listas de tamanho 3 é formada
    uma outra nova lista intercalando os elementos das duas
    lista-> lista"""
    lista = [] 
    lista.append ( lista1 [ 0 ] ) 
    lista.append ( lista2 [ 0 ] )
    lista.append ( lista1 [ 1 ] )
    lista.append ( lista2 [ 1 ] )
    lista.append ( lista1 [ 2 ] )
    lista.append ( lista2 [ 2 ] )
    return lista