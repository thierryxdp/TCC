def conta_frases(texto):
    """quantifica o numero de frases que aparecem em um texto fornecido pelo usuario.
assinatura: str --> int"""
    f = (str.replace(texto,"...","/"))
    e = (str.replace(f,"!","/"))
    i = (str.replace(e,"?","/"))
    r = (str.replace(i,".","/"))
    return str.count(r,"/")