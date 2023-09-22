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
        modificada = modificada[str.index(string, letra):]
        contagem = contagem + 1
    return len(original) - len(modificada) - 1