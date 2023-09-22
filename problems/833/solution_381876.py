def conta_numerofor(numero,matriz):
    '''
    A função retorna a quantidade
    de vezes que a Matriz tem
    determinado numero.
    int,list -> int
    '''
    contagem = 0
    valores = []
    r = 0
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            r = [matriz[l][c]]
            if numero in r:
                contagem += 1
        return contagem