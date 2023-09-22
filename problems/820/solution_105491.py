def posLetra(string, let, n):
    """Recebe string, uma letra e um número que indica a ocorrência da letra, retornando a posi-
    ção da string da ocorrência da letra. Caso haja menos ocorrências da letra que o número, retor-
    na '-1'
    assinatura: str, str, int --> int
    """
    a=len(string)
    indic=[map(string.index(a), string)]
    return indic