def conta_frases(frases):
    ''' Essa função calcula o número de frases contidas em um texto, str,str,int'''
    conta = str.join('/', str.split(frases, '...'))
    return str.count(conta,'/') + str.count(conta,'?') + str.count (conta,'!') + str.count (conta,".")