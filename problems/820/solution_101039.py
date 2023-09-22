def posLetra (string, letra, ocorrencia):
    """Retorna a posição da string relativa à ordem de ocorrência de uma dada letra.
    Entrada: str, str, int
    Saída: int
    """
    contagem = 0
    original = string
    modificada = string
    if str.count(string, letra) < ocorrencia:
        return -1
    while contagem < ocorrencia:
        modificada = modificada[str.index(frase, letra):]
        contagem = contagem + 1