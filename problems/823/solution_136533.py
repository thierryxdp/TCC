def faltante(l):
    '''
    A função retorna o número da peça faltante em um
    quebra-cabeça
    (entrada = list / saída = int)
    '''
    list.sort(l)
    i = 0
    n = 1
    while i < len(l):
        if not ([n] in l[i]):
            return n
        i += 1
        n += 1