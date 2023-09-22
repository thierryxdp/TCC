def repetidos(li):
    '''Recebe uma lista,li, e retorna o número
    de vezes em que o elemento é igual ao seu
    posterior
    list->int'''
    i=0
    rep=0
    while i<(len(li)-1):
        if li[i]==li[i+1]:
            rep=rep+1
        i=i+1
    return rep