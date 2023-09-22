def conta_numero(numero:int,matriz:list)-> int:
    """Função que, dado um número e uma
    matriz, calcula e retorna a quantidade de
    vezes que esse número aparece na matriz."""
    
    quant_numero = 0
    linhas = len(matriz)
    
    for i in range(linhas):
        coluna = matriz[i]
        for j in coluna:
            if numero == j:
                quant_numero += 1
    return quant_numero