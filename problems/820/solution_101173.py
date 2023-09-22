def posLetra (string, letra, n):
    """Retorna o índice da n-ésima ocorrência de uma dada letra numa dada string
    Entrada: str, str, int
    Saída: int
    """
    contagem = 0
    modificada = string
    original = string
    
    if str.count(string, letra) < n:
        return -1
    
    while contagem < str.count(string, letra):
        x = str.index(modificada, letra)
        modificada = modificada[x+1:]
        contagem += 1
    return len(original) - len(modificada)