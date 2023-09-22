def conta_numero(n, matriz):
    '''
    Inicia um contador. Varre as listas da matriz e
    verifica se nestas listas existe o elemento pedido.
    Caso exista, ele entra pra conta e retorna a soma.
    '''
    k = 0
    for x in matriz:
        k += x.count(n)

    return k