def conta_frases(texto):
    s=str(texto)
    str.replace("...",".") 
    return int(str.count(s,"!"))+int(str.count(s,"?"))+int(str.count(s,"."))