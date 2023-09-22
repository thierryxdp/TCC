def conta_frases(texto):
    l1=str.count(texto,"!")
    l2=str.count(texto,"?")
    l3=str.count(texto,"...")
    l4=[str.replace(texto,"...",".")]
    return l4