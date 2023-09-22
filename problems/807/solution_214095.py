def conta_frases(texto):
    texto_novo = str.replace(texto,'!','.')
    texto_novo = str.replace(texto_novo,'?','.')
    texto_novo = str.replace(texto_novo,'...','.')
    return len(str.split(texto_novo,'.'))