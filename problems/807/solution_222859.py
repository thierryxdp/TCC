def conta_frases(texto):
    ponto=str.count(texto, ".")
    exclamacao=str.count(texto, "!")
    interrogacao=str.count(texto, "?")
    reticencias=str.count(texto, "...")
    if "..." in texto:
        return (ponto+exclamacao+interrogacao-(reticencias*2)
         else:
                return (ponto+exclamacao+interrogacao+reticencias)