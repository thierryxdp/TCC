#-----------------EXERCICIO 3------------------------

def media_matriz(matriz):
    '''Retorna a média de todos os numeros da matriz
        ASSUME os elementos como números inteiros
        e a matriz não vazia
       list -> float'''
    
    soma = 0 #somatório de todos elementos da matriz até o momento
    elementos = 0 #conta a quantidade de elementos na matriz até o momento
    
    for contaLinha in range(len(matriz)):
        for contaColuna in range(len(matriz[contaLinha])):
            soma += matriz[contaLinha][contaColuna]
            elementos += 1
    
    return round(soma/elementos,2)