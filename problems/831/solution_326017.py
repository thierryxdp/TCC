def lingua_p(palavra):
    """Função que transforma as palavras em lingua do p"""
    final = ""
    contador = 0
    letra = palavra[contador]
    for letra in range(0,len(palavra)):
        if palavra[contador] in "aeiou":
            final = str(letra) + "p" + str(letra)
        final+= letra
        contador += 1
    return final