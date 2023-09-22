def uppCons(frase):
    """Dada uma frase retorna esta com suas consoantes em maiúsculo.
       str -> str"""

verificaVogais = 'AEIOUaeiouÂâÊêÎîÔôÛûÁáÉéÍíÓóÚúÀàÈèÌìÒòÙùÃãÕõ'
indiceFrase = 0

    while indiceFrase < len(frase):
        if frase[indiceFrase] not in verificaVogais:
            frase[indiceFrase].upper()
        indiceFrase = indiceFrase + 1
    return frase