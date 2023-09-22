def posLetra(string, let, n):
    """Recebe uma string, uma letra e um valor que indica a ocorrência da letra, retornando
    a posição dela na string.
    assinatura:
    tuple (str, str, int) -> int
    """
    if str.count(string, let)<n:
        return -1
    else:
        return string.index(let)