def faltante(lista):
    '''Função que,dada uma lista, descobre qual número inteiro deste intervalo está faltando.
    lista-->int'''
    i = 0
    faltante = ''
    listateste = ''
    listateste = [listateste]
    while i<len(lista):
        listateste[i]=i
        if lista == listateste:
            faltante = lista[i]+1
        if lista[i]!=listateste[i]:
            faltante = (lista[i-1]+lista[i])/2
        i = i+1
    return faltante