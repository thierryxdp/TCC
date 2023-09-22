def conta_numero(numero,matriz):
    posicao=0
    while posicao < len(matriz):
        quantidade=list.count(matriz[posicao], numero)
        posicao+=1
    return quantidade