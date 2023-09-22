def posLetra(string, let, n):
    """Recebe uma string, uma letra e um valor que indica a ocorrência da letra, retornando
    a posição dela na string.
    """
    indec=[string.index(let) for let in string]
    
    if str.count(string, let)<n:
        return -1
    else:
        return indec