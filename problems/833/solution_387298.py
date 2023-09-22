def conta_numero(numero,matriz):
    '''funçao que dada um numero e uma matriz de inteiros, conta
e retornar quantas vezes esse numero aparece na matriz.
list -> int'''
    contador=0
    for linha in matriz:
        for coluna in linha:
            if numero == coluna:
                contador+=1
    return contador