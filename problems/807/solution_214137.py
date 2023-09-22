def conta_frases(texto):
    l1=str.count(texto,"!")
    l2=str.count(texto,"?")
    lista=[str.replace(texto,"...",".")]
    return l1+l2+str.count(lista,".")