def conta_numero(numero,matriz):
    posicao=0
    col=matriz[posicao]
    while posicao < len(matriz):
        quantidade=col.count(numero)
        posicao+=1
        return quantidade