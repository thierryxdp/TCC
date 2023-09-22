def conta_frases(texto):
    ponto=str.count(texto, ".")
    exclamaçao=str.count(texto, "!")
    interrogaçao=str.count(texto,"?")
    reticencias=str.count(texto, "...")
    if  "..." in texto: 
        return (ponto+exclamaçao+interrogaçao-(reticencias*2))
    else:
        return (ponto+exclamaçao+interrogaçao+reticencias)