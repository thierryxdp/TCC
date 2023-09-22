def conta_frases(texto):
    texto_2=str.replace(texto,"...",".")
    ponto=str.count(texto_2,".",0,len(texto))
    exclamacao:str.count(texto_2,"!",0,len(texto))
    interrogacao:str.count(texto_2,"?",0,len(texto))
    return ponto+exclamacao+interrogacao