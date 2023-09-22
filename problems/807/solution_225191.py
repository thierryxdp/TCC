def conta_frases(frases):
    '''crie uma função que, dado um texto armazenado em uma string, retorne o número de frases que aparecem neste texto mediante as pontuações presentes nele. str-->str.'''
    x = str.count(frases,'...')
    y = str.count(frases, '.')
    z = str.count(frases, '?')
    w = str.count(frases, '!')
    return (y + z + w) - 2*x