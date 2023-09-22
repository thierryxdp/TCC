#Questão2
def conta_numero(numero,matriz):
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
            list.append(valores, matriz[l][c])
    while r < len(valores):
        if numero == valores[r]:
            contagem += 1
        r = r + 1
    return contagem