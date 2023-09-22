conta_numero (numero, matriz):
    """Funcao que dada uma matriz de inteiros de tamanho qualquer e um numero inteiro, conta eretorna quantas vezes aquele n´umero aparece na matriz."""
    counter = 0
    for lista in Matriz:
        
        for elem in lista:
            if elem == numero:
                counter +=1
    return counter