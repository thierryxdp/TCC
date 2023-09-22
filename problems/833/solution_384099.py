def conta_numero (numero: int,matriz: list) -> int:
    """Função que dada um número inteiro e uma matriz de interios de qualquer tamanho, conta e retorna o números de vezes que o número aparece na matriz."""
    contador = 0
    for i in range(len(matriz)):
        if numero == i:
            contador += 1
    for j in range(len(matriz[0])):
         if numero == j:
            contador += 1
    return contador