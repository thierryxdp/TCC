def conta_frases(frase):
    if not str.find(frase,"..."):
        a=str.count(frase, ".")
        b=str.count(frase, "!")
        c=str.count(frase,"?")
        return a+b+c
    
    else:
        a=str.count(frase,".")-str.count(frase,"...")+1
        b=str.count(frase, "!")
        c=str.count(frase,"?")
        return a+b+c