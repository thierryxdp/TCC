def conta_frases (texto):
    texto=str.replace(texto,'...','.')
    texto=str.replace(texto,'?','.')
    texto=str.replace(texto,'!','.')
    
    return texto.count('.')