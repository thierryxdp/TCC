def conta_frases(frase):
    lista = str.split(frase)
    a=str.count(lista,"...")
    b=str.count(lista,"!")
    c=str.count(lista,"?")
    d=str.count(lista,".")
    result=a+b+c+d 
    return result