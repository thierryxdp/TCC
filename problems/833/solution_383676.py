def conta_numero(numero,matriz):
    '''Função que dado um número inteiro e uma matriz de inteiros de
    tamanho qualquer, conta e retorna quantas vezes aquele número 
    aparece na matriz.
    int, matriz->int'''
    
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            aparicoes=(matriz[i]).count(numero)
    
    return aparicoes