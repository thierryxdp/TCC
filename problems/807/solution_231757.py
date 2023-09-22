def conta_frases(frase):
    return (str.count(frase, ".") - (2*(str.count(frase, "..."))/3) + str.count(frase, "!") + str.count(frase, "?"))