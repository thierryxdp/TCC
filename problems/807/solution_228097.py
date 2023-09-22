def conta_frases(texto):
    texto=str.replace(texto,'...','.')
    texto=str.replace(texto,'!','.')
    texto=str.replace(texto,'?','.')
    texto=str.split(texto,'.')
    texto=list.remove(texto,'')
    qtd=len(texto)
    return qtd