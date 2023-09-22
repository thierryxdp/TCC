def repetidos(l):
    '''
    A função retorna o número de vezes que um elemneto era 
    igual ao anterior
    (entrada = list / saída = int)
    '''
    i = 1 
    c = 0
    while i < len(l):
        if l[i] == l[i -1]:
            c += 1
        i += 1
    return c