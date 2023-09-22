def conta_numero(numero,matriz):
    resposta = 0 
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numero == j:
                resposta = resposta + 1
    return resposta