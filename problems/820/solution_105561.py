def posLetra(string, let, n):
    """Recebe stringm uma letra e um valor que indica a ocorrência da letra, retornando
    a posição dela na string.
    """
    
    indic= string[str.index(string, let, n,n+1)]
    if str.count(string, let)<n:
        return -1
    else:
        return indic