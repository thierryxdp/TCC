def conta_frases(texto):
    l1=str.count(texto,"!")
    l2=str.count(texto,"?")
    lista=[str.replace(texto,"...",".")]
    l3=str.count(lista,".")
    return l1+l2+l3