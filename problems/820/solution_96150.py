def posLetra(frase, letra, n):
    """finção que recebe como entrada uma string, uma letra e um número
que indica a ocorrência desejada da letra e retorna em que posição
da string aquela ocorrência da letra está."""
    posicao = frase.find(letra)
    while posicao >= 0 and n > 1:
        posicao = frase.find(letra, posicao + 1)
        n = n-1
    return posicao