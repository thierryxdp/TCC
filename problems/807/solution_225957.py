def conta_frases(texto):
    if "…"in texto:
        str.replace(texto,"…","!")
    
    exclamacao=str.count(texto,"!")
    interrogacao=str.count(texto,"?")
    reticencia=str.count(texto,"…")
    return exclamacao+interrogacao+reticencia