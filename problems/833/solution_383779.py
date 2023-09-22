def conta_numero(numero,matriz):
    resposta = 0 
    for i in range(len(matriz)):
        lista = matriz[i]
        n = lista.count(numero)         
        resposta = resposta + n 
    return resposta