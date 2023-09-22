def colchao(lista,h,l):
    '''Funcao que retorna se possivel passar o colchao'''
    if h>l:
        if l>=lista[0] and h>=lista[1]:
            return True
    else:
        if h>lista[0] and l>lista[1]:
            return True
    return False