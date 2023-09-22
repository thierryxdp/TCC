def conta_frases(texto):
    texto=str.replace(texto,'...','.')
    texto=str.replace(texto,'!','.')
    texto=str.replace(texto,'?','.')
    texto=str.split(texto,'.')
    qtd=len(texto)-1
    return qtd