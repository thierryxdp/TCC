def uppCons(frase):
    saida = ""
    for letra in frase:
        if letra not in "aeiouAEIOU":
            saida = saida + letra.upper()
        
    return saida