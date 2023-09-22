def conta_numero(numero,matriz):
    " " "Dado um numero inteiro e uma matriz de inteiros de tamanho qualquer, conta e retorna quantas vezes aquele número aparece na matriz:int, list, -> int " " "
    resposta = 0 
    for i in range(len(matriz)):
        lista = matriz[i]
        n = lista.count(numero)         
        resposta = resposta + n 
    return resposta