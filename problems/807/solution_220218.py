def conta_frases(texto):
    """calcula e retorna quantas frases há em um texto"""
    .="."
    ...="..."
    a= str.count(texto,".")
    b=str.count(texto,"!")
    c=str.count(texto,"?")
    d=str.count(texto,"...")
    return a+b+c+d