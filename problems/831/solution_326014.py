def lingua_p(palavra):
    """Função que transforma as palavras em lingua do p"""
    final = ""
    contador = 0
    letra = palavra[contador]
    for letra in range(0,len(palavra)):
        if letra in "aeiou":
            final = letra + "p" + letra
        final+= letra
        contador += 1
    return final