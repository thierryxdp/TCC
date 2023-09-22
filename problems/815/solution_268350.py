def insere ( lista_numero, n ):
    """Função que dada uma lista ordenada de numeros inteiros e um numero n 
    inclua n na posição correta , de maneira que a lista continue ordanada
    in, int --> int"""
    desordem = [ ] list.insert( lista_numero, n)
    ordem = list.sort(desordem)
    return ordem