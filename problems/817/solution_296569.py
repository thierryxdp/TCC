def media(l):
    '''
    A função retorna todas as notas maiores que a média
    (entrada = list / saída = list)
    '''
    f = []
    m = sum(l) / len(l)
    for x in l:
        if x > m:
            list.append(f, x)
    list.sort(f)
    return f