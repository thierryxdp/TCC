def conta_numero(numero: int, matriz: list)-> int:
    """Dado um número inteiro (n) e uma matriz de inteiros de tamanho
    qualquer, a função retorna quantas vezes "n" aparece na matriz"""
    contador = 0
    numlinhas = len(matriz)
    numcolunas = len(matriz[0])
    for i in range(numlinhas):
        for j in range(numcolunas):
            if numero == matriz[i][j]:
                contador += 1
    return contador