def conta_frases(frase):
    ls1=str.split(frase,".")
    ls2=str.split(frase,"!")
    ls3=str.split(frase,"?")
    ls4=str.split(frase,"...")
    return len(ls1) and len(ls2) and len(ls3) and len(ls4)