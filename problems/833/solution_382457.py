def conta_numero(numero,matriz):
    """dada uma matriz e um número, a função retorna o número de vezes
    que o numero aparece na matriz.
    int, list--> list
    
    Parâmetros
    indice1= índice do primeiro while
    indice2: índice do segundo while
    numero: número a ser procurado na matriz
    matriz: matriz em que o número irá ser procurado"""
    indice1=0
    contagem=0
    while indice1<len(matriz):
        indice2=0
        while indice2<len(matriz[0]):
            if matriz[indice1][indice2]==numero:
                contagem=contagem+1
            indice2=indice2+1
        indice1=indice1+1
    return contagem