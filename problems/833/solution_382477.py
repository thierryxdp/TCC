def conta_numero(numero, matriz):
    """Funcao que retorna o numero de vezes que um numero se encontra
    dentro de uma matriz especificada.
    Entrada: int, list(list);
    Saida: int
    
    Parameters:
    numero: numero inteiro a ser contado da matriz;
    matriz: lista com as listas da matriz."""
    n_vezes = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                n_vezes += 1
    return n_vezes