def conta_frases(texto):
     texto=str.replace(texto,'?','.')
     texto=str.replace(texto,'!','.')
     texto=str.replace(texto,'...','.')
     f=str.count(texto,'.')
     return f