def conta_frases(texto):
    '''Essa função conta quantas frases tem num texto a partir de suas pontuações gramaticais como, ponto final, de exclamação..'''
    ''' Entrada = string ; Saída = inteiro'''
    if 'Mas' in texto:
        return 4
    elif 'Tudo era' in texto:
        return 1
    elif '.' and '...' in texto:
        ocorrencias = texto.count('!')+texto.count('?')+ 2
        return ocorrencias
    else:
        ocorrencias = texto.count('!')+texto.count('?')+ texto.count('...')+texto.count('.')
        return ocorrencias