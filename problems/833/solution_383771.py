def conta_numero(numero,matriz):
    '''Entre com um numero e uma matriz para contar quantas vezes esse
    numero está na matriz
    Int, Matriz -> Int'''
    cont=0
    for x in range(matriz):
        if x == numero:
            cont=cont+1     
    return cont