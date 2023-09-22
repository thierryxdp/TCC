def conta_frases(texto):
    textonovo=str.replace(texto,"...", ".")
    return textonovo.count('!')+textonovo.count('?')+textonovo.count('.')