def conta_frases(texto):
    s=str(texto)
    return str.count(s,"!",0),str.count(s,"?",0),str.count(s,"...",0),str.count(s,".!",0)