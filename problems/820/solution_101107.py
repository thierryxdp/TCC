def posLetra (string, letra, n):
    """Retorna o índice da n-ésima ocorrência de uma dada letra numa dada string
    Entrada: str, str, int
    Saída: int
    """
    contagem = 0
    original = string
    modificada = string
    a = str.index(string, letra)
    if str.count(string, letra) < n:
        return -1
    while contagem < str.count(string, letra):
        modificada = str.index(string, letra, a, -1)
        contagem += 1
    return len(original) - len(modificada)