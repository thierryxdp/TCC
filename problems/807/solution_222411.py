def conta_frases(texto):
    """retorna a quantidade de frases em um texto. str->int"""
    ponto=str.count(texto, ".")
    exclamaçao=str.count(texto, "!")
    interrogaçao=str.count(texto,"?")
    reticencias=str.count(texto, "...")
    if  "..." in texto: 
        return (ponto+exclamaçao+interrogaçao+reticencias-3)
    else:
        return (ponto+exclamaçao+interrogaçao+reticencias)