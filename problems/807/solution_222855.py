def conta_frases(texto):
    ponto=str.count(texto, "isso e bonito.")
    exclamacao=str.count(texto, "meu deus!")
    interrogacao=str.count(texto, "o que?")
    reticencias=str.count(texto, "gente...")
    if "gente..." in texto:
        return (ponto+exclamacao+interrogacao-(reticencias*2)
                else: return (ponto+exclamacao+interrogacao+reticencias)