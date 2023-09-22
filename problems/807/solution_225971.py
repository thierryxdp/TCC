def conta_frases(texto):
    if "…" in texto:
     novo=str.replace(texto,"...","a.b") 
        
    ponto=str.count(texto,".")
    exclamacao=str.count(texto,"!")
    interrogacao=str.count(texto,"?")
    reticencia=str.count(texto,"…")
    return novo