def conta_numero(numero, matriz):
    """Função que dado um número inteiro e uma matriz de números inteiros
    de qualquer tamanho, conta e retorna quantas vezes esse número aparece
    na matriz.
    int,mat->int
    """
    contagem = 0
    for linha in matriz:
        for coluna in matriz:
            if numero==coluna:
                contagem = contagem + 1
    return contagem