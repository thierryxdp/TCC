def conta_frases(frase):
    a=str.count(frase,".")
    b=str.count(frase,"!")
    c=str.count(frase,"?")
    d=str.count(frase,'...')
    result=a+b+c+d 
    return result