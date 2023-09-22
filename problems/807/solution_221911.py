def conta_frases(frase):
    
    a=str.count(frase,".")
    b=str.count(frase,"!")
    c=str.count(frase,"?")
    if a<=1:
        return a+b+c 
    elif a>1:
        return a-2+b+c