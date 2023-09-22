def conta_frases(texto):
    '''Essa função conta quantas frases tem num texto a partir de suas pontuações gramaticais como, ponto final, de exclamação..'''
    ''' Entrada = string ; Saída = inteiro'''
    ocorrencias = texto.count('. ')+texto.count('!')+texto.count('?')+texto.count('...')
    return ocorrencias