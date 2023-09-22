def conta_frases(texto):
    "retorna o número de frases em um conjunto de frases"
    "str -> int"
    aux=0
    aux=aux+str.count(texto,".", 0)
    aux=aux+str.count(texto,"!",0)
    aux=aux+str.count(texto,"?",0)
    aux=aux+str.count(texto,"...",0)
    return aux