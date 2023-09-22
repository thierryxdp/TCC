def uppCons(frase):
    saida = ""
    for letra in frase:
        if letra not in "aeiouAEIOU":
            saida = saida + letra.upper()
        else:
            saida = saida + letra.lower()
    return saida