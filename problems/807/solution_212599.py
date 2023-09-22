def conta_frases(frase):
    a=str.count(frase, ".")-(str.count(frase,"..."))+1
    b=str.count(frase, "!")
    c=str.count(frase,"?")
    return a+b+c