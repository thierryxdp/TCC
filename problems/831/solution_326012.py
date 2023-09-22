def lingua_p(palavra):
    """Função que transforma as palavras em lingua do p"""
    final = ""
    contador = 0
    varredura = palavra[contador]
    for letra in range(0,len(palavra)):
        if palavra[contador] in "aeiou":
            final = varredura + "p"+ letra
        final+= varredura
        contador += 1
    return final