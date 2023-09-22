def colchao (medida ,H,L):
    """Essa função iráretornar se o colchão passará ou não pela porta ; lista -> booleano"""

    if (H * L) <= medida:
        return "True"

    else:
        return "False"