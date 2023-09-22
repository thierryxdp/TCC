def conta_numero(numero: int, matriz: list)-> int:
    """ Dado um número inteiro e uma matriz, retorna quantas
    vezes esse número aparece na matriz."""
    
    linhas = len(matriz)
    qtd_numero = 0
    
    if (len(matriz) == 0):
        return 0
    
    else:
        colunas = len((matriz)[0])
    
        for i in range(linhas):
            for j  in range(colunas):
                if (matriz[i][j] == numero):
                    qtd_numero += 1
                
        return qtd_numero