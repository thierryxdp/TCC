def conta_frases(texto):
    contador1 = len(texto.split('.'))
    contador2 = len(texto.split(','))
    contador3 = len(texto.split('!'))
    contador4 = len(texto.split('?'))
    contador5 = len(texto.split('...'))
    return contador1+contador2+contador3+contador4+contador5