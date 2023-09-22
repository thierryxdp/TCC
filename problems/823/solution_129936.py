def faltante(l):
    '''
    Retorna qual a peça do quebra-cabeça
    esta faltando.
    list -> int
    '''
    
    l.sort()
    i = 0
    while i < len(l):
        if i + 1 != l[i]:
            return i + 1
        i = i + 1
    return len(l) + 1