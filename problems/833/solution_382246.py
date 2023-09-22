def conta_numero(numero,matriz):
    '''
    A função retorna a quantidade
    de vezes que a Matriz tem
    determinado numero.
    int,list -> int
    '''
    contagem = 0
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if numero == matriz[l][c]:
                contagem += 1
    return contagem