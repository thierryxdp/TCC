def conta_frases(texto):
    """função que receba um texto e retorne a quantidade de frases que o texto contem ,sabendo que a cada frase do texto  é terminada por ponto(. ou ... ou ? ou !)
    str->int"""
    if "..." in texto:
        novo=str.replace(texto,"...","a.b")
        ponto=str.count(novo,".")
        exclamacao=str.count(novo,"!")
        interrogacao=str.count(novo,"?")
        reticencia=str.count(novo,"…")
        return ponto+exclamacao+interrogacao+reticencia
        
     
    else:
        ponto=str.count(texto,".")
        exclamacao=str.count(texto,"!")
        interrogacao=str.count(texto,"?")
        reticencia=str.count(texto,"…")
        return ponto+exclamacao+interrogacao+reticencia