def repetidos(l):
    '''funcao que retorna o numero de vezes que um elemento
    da lista é igual ao elemento anterior'''
    f=0
    g=0
    while f<len(l):
        if l[f]==l[f-1]:
            g=g+1
        f=f+1
    return g