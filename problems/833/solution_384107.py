def conta_numero (numero: int,matriz: list) -> int:
    """Função que dada um número inteiro e uma matriz de inteiros de qualquer tamanho, conta e retorna o números de vezes que o número aparece na matriz."""
    contador = 0
    i = len (matriz)
    j = len (matriz[0])
    for n in range(matriz[i]):
        if n == numero:
            contador += 1
        for n in range (matriz[i][j]):
            if n == numero:
                contador +=1
    return contador