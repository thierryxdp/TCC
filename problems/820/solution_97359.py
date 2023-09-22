def posLetra (frase: str,letra: str,numero: int) -> int:
    """Função que recebe uma frase, uma letra e um número referente à ocorrência desejada da letra
    e retorna a posição da string que aquela ocorrência está. Caso exista menos ocorrências do
    que a ocorrência desejada, o retorno será -1."""
    posicao = frase.find(letra)
    while posicao >= 0 and numero >1:
        posicao = frase.find(letra, posicao +1)
        numero -= 1
    return posicao