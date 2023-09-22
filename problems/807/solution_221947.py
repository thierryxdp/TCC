def conta_frases(frase):
    a=str.count(frase,".")
    b=str.count(frase,"!")
    c=str.count(frase,"?")
    if a<=2:
        return a+b+c