def conta_frases(texto):
    result = len(texto.split('?'))
    result2 = len(texto.split('.'))
    result3= len(texto.split('...'))
    result4 = len(texto.split('!'))
    restulttotal = result + result2 + result3 + result4 
    return resulttotal