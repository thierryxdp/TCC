def posLetra(string, let, n):
    """Recebe string, uma letra e um número que indica a ocorrência da letra, retornando a posi-
    ção da string da ocorrência da letra. Caso haja menos ocorrências da letra que o número, retor-
    na '-1'
    assinatura: str, str, int --> int
    """
    indic=[x[i] for x in string]
    return indic