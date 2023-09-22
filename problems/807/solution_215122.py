def conta_frases(texto):
    quantidade1= len(texto.split('.'))
    quantidade2= len(texto.split('!'))
    quantidade3= len(texto.split('?'))
    quantidade4= len(texto.split('...'))
    return quantidade1+quantidade2+quantidade3+quantidade4