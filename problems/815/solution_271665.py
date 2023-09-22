def insere(lista_numero:list[int],n:int)->list[int]:
    '''Insere n na sua respectiva posição dentro da lista
    de números ordenada.'''
    listaNumeroOrdenada.append(n)
    listaNumeroOrdenada.sort()
    
    return listaNumeroOrdenada