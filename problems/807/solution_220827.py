def conta_frases(frases):
    result = len(frases.split('.'))
    result2 = len(frases.split('!'))
    result3 = len(frases.split('...'))
    result4 = len(frases.split('?'))
    result = result - 1
    result2 = result2 - 1
    result4 = result4 - 1
    contador = result + result2 + result3 + result4
    return result2