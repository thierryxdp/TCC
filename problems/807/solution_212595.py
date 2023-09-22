def conta_frases(frase):
    a=str.find(frase, ".")
    b=str.count(frase, "!")
    c=str.count(frase,"?")
    return a+b+c