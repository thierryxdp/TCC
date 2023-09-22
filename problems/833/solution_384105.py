def conta_numero (numero: int,matriz: list) -> int:
    """Função que dada um número inteiro e uma matriz de inteiros de qualquer tamanho, conta e retorna o números de vezes que o número aparece na matriz."""
    contador = 0
    nlinhas = len (matriz)
    
    for numero in matriz[range(nlinhas)]:
        contador +=1
    return contador