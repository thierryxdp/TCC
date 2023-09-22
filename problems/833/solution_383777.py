def conta_numero(numero,matriz):
    resposta = 0 
    for i in len(matriz):
        for j in len(matriz[i]):
            if numero == j:
                resposta = resposta + 1
    return resposta