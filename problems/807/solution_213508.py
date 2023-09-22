def conta_frases(texto):
    """essa função retorno quantas frases tem em um texto"""
    """string->int"""
    s=str(texto)
    f=str.replace(s,"...",".") 
    return int(str.count(f,"!"))+int(str.count(f,"?"))+int(str.count(f,"."))