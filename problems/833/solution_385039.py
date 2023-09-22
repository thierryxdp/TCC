def conta_numero(numero,matriz):
    """Função que busca e retorna quantas vezes um número aparece numa lista"""
    """Int, List -> Int"""
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                total += 1                
    return total