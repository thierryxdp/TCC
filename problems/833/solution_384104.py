def conta_numero (numero: int,matriz: list) -> int:
    """Função que dada um número inteiro e uma matriz de interios de qualquer tamanho, conta e retorna o números de vezes que o número aparece na matriz."""
    contador = 0
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    for i in range(nlinhas):
        for j in range(ncolunas):
            if numero == j:
                contador += 1
    return contador