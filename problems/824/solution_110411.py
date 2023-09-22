def uppCons(frase):
    saida = ""
    for letra in frase:
        if letra not in "aeiouAEIOU":
            saida = saida + letra.upper()+frase
        else:
            saida = saida + letra.lower()
    return saida