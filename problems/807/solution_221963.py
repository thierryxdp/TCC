def conta_frases(frase):
    a=str.count(frase,"...")
    b=str.count(frase,"!")
    c=str.count(frase,"?")
    d=str.count(frase,".")
    if a!=0:
        return a+b+c+d-3