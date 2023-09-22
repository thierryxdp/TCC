def uppCons(frase):
    """Dada uma frase retorna esta com suas consoantes em maiúsculo.
       str -> str"""

    verificaVogais = 'AEIOUaeiouÂâÊêÎîÔôÛûÁáÉéÍíÓóÚúÀàÈèÌìÒòÙùÃãÕõ'
    indice = 0
    fraseAlterada = ' '
    letras = list(frase)

    while indice < len(frase):
        if letras[indice] not in verificaVogais:
            frase[indice].upper()
            fraseAlterada += frase[indice]
        indice = indice + 1
    return frase