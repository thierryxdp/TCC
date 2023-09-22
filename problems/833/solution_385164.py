def conta_numero(numero,matriz):
    """ Função que retorna a quatidade de "numero" dentro a "matriz" de entrada: int, matriz/int-> int"""
    
    contador = 0
    
    for indice1 in range(len(matriz)):
        for indice2 in range(len(matriz[0])):
            if matriz[indice][indice2] == numero:
                contador += 1
    
    return contador