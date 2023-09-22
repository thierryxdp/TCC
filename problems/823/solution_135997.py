def faltante(lista):
    '''
    funcao retorna o termo faltante na lista
    '''
    s=0
    p = 0
    while p < (len(lista)+1):
        s=s+(1+p)
        p = p + 1
    return s-sum(lista)