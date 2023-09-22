def conta_frases(frase):
    a=str.count(frase,".")
    b=str.count(frase,"!")
    c=str.count(frase,"?")
    if a<=2:
        return a+b+c 
    else:
        if a>=3:
            return a-2+b+c