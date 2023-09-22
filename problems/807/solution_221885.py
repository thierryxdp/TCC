def conta_frases(frase):
    lista= str.split(frase)
    a=list.count(lista,".")
    b=list.count(lista,"!")
    c=list.count(lista,"?")
    d=list.count(lista,"...")
    return a+b+c+d