def insere(lista_numero:list[int],n:int)->list[int]:
    '''Insere n na sua respectiva posição dentro da lista
    de números ordenada.'''
    l1 = listaNumeroOrdenada.append(n)
    l2 = l1.sort()
    
    return l2