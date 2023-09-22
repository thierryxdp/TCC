def conta_numero(numero,matriz):
    col=matriz[posicao]
    posicao=0
    while posicao < len(matriz):
        quantidade=col.count(numero)
        posicao+=1
        return quantidade