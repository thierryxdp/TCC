def conta_frases(texto):
    frases1 = len(texto.split('.'))
    frases2 = len(texto.split('!'))
    frases3 = len(texto.split('?'))
    frases4 = len(texto.split('...'))
    
    qntfrases= frases1 + frases2 +frases3+frases4
    return qntfrases