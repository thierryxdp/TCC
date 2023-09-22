def conta_numero (num, matriz):
    '''Função que dado um numero inteiro e uma matriz de inteiros de qualquer tamanho    
    conta e retorna quantas vezes aquele numero aparece na matriz
    float, list -> int '''
    cont = 0
    for lista_numero in matriz:
        for numero in lista_numero:
            if numero == num:
                cont=cont + 1
    return cont