#Questão2
def conta_numero(numero,matriz):
    '''
    A função retorna a quantidade
    de vezes que a Matriz tem
    determinado numero.
    int,list -> int
    '''
    contagem = 0
    numero = list(numero)
    valores = []
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            list.append(valores, matriz[l][c])
            if numero in valores:
                contagem += 1
    return len(valores)