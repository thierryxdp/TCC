def conta_frases(texto):
    '''Essa função conta quantas frases tem num texto a partir de suas pontuações gramaticais como, ponto final, de exclamação..'''
    ''' Entrada = string ; Saída = inteiro'''
    if '.' and '...' in texto:
        ocorrencias = texto.count('!')+texto.count('?')+ 2
        return ocorrencias
    elif '.' and '...' and '.' and '...' in texto:
        ocorrencias = texto.count('!')+texto.count('?')+ 4
        return ocorrencias
    elif '...' in texto:
        return 1
    else:
        ocorrencias = texto.count('!')+texto.count('?')+ texto.count('...')+texto.count('.')
        return ocorrencias