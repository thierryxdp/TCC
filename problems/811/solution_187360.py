def colchao(m, h, l):
    '''Função que compara o colchão com a porta'''
    if m[1]<=h:
        return True
    elif m[1]<l:
        return True
    else:
        return False