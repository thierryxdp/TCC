def quant_palavras(frase):
    """Recebe uma frase e retorna o número de palavras
dela.
str -> int
"""
    sem_espacos_laterais = str.strip(frase)
    n_de_palavras = str.count(sem_espacos_laterais, " ")
    return n_de_palavras + 1