def conta_frases(texto):
    texto = texto.split(.)
    texto = texto.split(!)
    texto = texto.split(?)
    texto = texto.split(...)
    texto = str.count(texto,'.')+str.count(texto,'!')+str.count(texto,'?')+str.count(texto,'...')
    return texto