def conta_numero(numero,matriz):
    """
    Função que recebe um número e uma matriz, com isso, conta e retorna quantas vezes aquele 
    número aparece na matriz.
    int, list -> int
    """
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    soma = 0
    
    for i in range(linhas):
        for j in range(colunas):
            if numero == i or numero == j:
                soma += 1
    return soma