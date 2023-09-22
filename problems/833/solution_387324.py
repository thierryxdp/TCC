def conta_numero(numero,matriz):
    '''Dada um número inteiro e uma matriz de inteiros de tamanho qualquer, e retorna quantas vezes aquele número aparece na matriz
    int,list->int'''
    
    for a in range(len(matriz)):
        contador=0
        for b in range(len(matriz[a])):
            if numero in matriz[a]:
                contator+=1
                  
    return contador