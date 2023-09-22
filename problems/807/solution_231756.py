def conta_frases(frase):
    fim = {"." : ".", "!" : ".", "?" : ".", "..." : "." }
    return (str.count(frase, ".") - (2*str.count(frase, "...")/3) + str.count(frase, "!") + str.count(frase, "?"))