def uppCons(frase):
    """Dada uma frase retorna esta com suas consoantes em maiúsculo.
       str -> str"""

verificacao_vogais = 'AEIOUaeiouÂâÊêÎîÔôÛûÁáÉéÍíÓóÚúÀàÈèÌìÒòÙùÃãÕõ'
indice_frase = 0

    while indice_frase < len(frase):
        if frase[indice_frase] not in verificacao_vogais:
            frase[indice_frase].upper()
        indice_frase = indice_frase + 1
    return frase