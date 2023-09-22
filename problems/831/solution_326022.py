def lingua_p(palavra):
    """Função que transforma as palavras em lingua do p"""
    final = ""
    contador = 0
    letra = palavra[contador]
    for string in range(0,len(palavra) + 1):
        if palavra[contador] in "aeiou":
            final += letra + "p" + letra
        final+= letra
        contador += 1
    return final