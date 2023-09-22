def conta_frases(texto):
    ponto=str.count(texto,".")
    exclamacao+=str.count(texto,"!")
    interrogacao=str.count(texto,"?")
    reticencia=str.count(texto,"...")
    return ponto+exclamacao+interrogacao+reticencia