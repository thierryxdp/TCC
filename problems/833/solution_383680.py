def conta_numero(numero,matriz):
    '''Função que dado um número inteiro e uma matriz de inteiros de
    tamanho qualquer, conta e retorna quantas vezes aquele número 
    aparece na matriz.
    int, matriz->int'''
    
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            aparicoes=(matriz[i]).count(numero)
        contador = contador + aparicoes
    return contador