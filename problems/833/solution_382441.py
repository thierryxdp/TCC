#int,list(int)->int
def conta_numero(numero,mariz):
    "Função que dado um número inteiro e uma matriz de inteiros de tamanho qualquer, conta e retorna quantas vezes aquele número aparece na matriz"
    contador = 0
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            if matriz[i][j]==0:
                contador = contador+1
    return contador