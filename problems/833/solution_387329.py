def conta_numero(numero,matriz):
    '''Dada um número inteiro e uma matriz de inteiros de tamanho qualquer, e retorna quantas vezes aquele número aparece na matriz
    int,list->int'''
    
    contador=0

    for a in range(len(matriz)):
        if numero in matriz[a]:
            contador+=(list.count(matriz[a],numero)
                  
    return contador