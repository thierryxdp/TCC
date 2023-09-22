def lingua_p(palavra):
    """Função que transforma as palavras em lingua do p"""
    final = ""
    contador = 0
    letra = palavra[contador]
    for varredura in range(0,len(palavra) + 1):
        if palavra[contador] in "aeiou":
            final += palavra[contador] +"p"+ palavra[contador]
        final = final + palavra[contador]
        contador += 1
    return final