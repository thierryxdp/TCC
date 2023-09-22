def faltante(lista):
    '''Dada uma lista de N-1 inteiros, retorna o inteiro faltante'''
    list.sort(lista)
    a = 0
    proximo = 0
    if len(lista)== 1 and lista[0]== 1:
        return 2
    list.insert(lista,0,0)
    b = (lista[a+1]-1)
    while proximo < len(lista):
        if b in lista:
          a = a+1
          b = (lista[a]+1)
        proximo = proximo + 1
    return b