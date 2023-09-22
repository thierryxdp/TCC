def conta_frases(texto):
    ponto=str.count(texto, "isso e bonito.")
    exclamaçao=str.count(texto, "meu deus!")
    interrogaçao=str.count(texto, "o que?")
    reticencias=str.count(texto, "gente...")
    if "gente..." in texto:
        return (ponto+exclamaçao+interrogaçao-(reticencias*2)
                else:
                return (ponto+exclamaçao+interrogaçao+reticencias)