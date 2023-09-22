def uppCons(frase):
    """Dada uma frase retorna esta com suas consoantes em maiúsculo.
       str -> str"""

    vogais = 'AEIOUaeiouÂâÊêÎîÔôÛûÁáÉéÍíÓóÚúÀàÈèÌìÒòÙùÃãÕõ'
    contador = 0
    alterada = ' '
    letras = list(frase)

    while contador < len(frase):
        if letras[contador] not in vogais:
            frase[contador].upper()
            alterada += frase[contador]
        contador = contador + 1
    return alterada