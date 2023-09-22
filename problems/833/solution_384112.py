def conta_numero (numero: int,matriz: list) -> int:
    """Função que dada um número inteiro e uma matriz de inteiros de qualquer tamanho, conta e retorna o números de vezes que o número aparece na matriz."""
    contador = 0
    for i in range (len (matriz)):
        for j in range (len (matriz[0])):
            if matriz[i][j] == numero:
                contador += 1
    return contador