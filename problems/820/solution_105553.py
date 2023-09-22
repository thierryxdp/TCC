def posLetra(string, let, n):
    """Recebe stringm uma letra e um valor que indica a ocorrência da letra, retornando
    a posição dela na string.
    """
    indec=[string.index(let) for let in string]
    indic = dict(zip(indec), list(range(0, len(indec))))
    if str.count(string, let)<n:
        return -1