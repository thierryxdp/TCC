def conta_frases(texto):
    texto = texto.split(.)
    texto = texto.split(!)
    texto = texto.split(?)
    texto = texto.split(...)
    return str.count(texto,'.')+str.count(texto,'!')+str.count(texto,'?')+str.count(texto,'...')