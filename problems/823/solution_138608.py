def faltante(inteiros):
    '''retorna a peca que falta para completar o quebra cabeca
    list --> int'''
    i=0
    n=0
    list.sort(inteiros)
    falta=inteiros[len(inteiros)-1]+1
    while i<len(inteiros):
        if 1+n not in inteiros:
            falta=n+1
        i=i+1
        n=n+1
    return falta