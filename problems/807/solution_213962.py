conta_frases(texto):
    '''dado um texto, essa função conta o número de frases que esse texto possui. str->int'''
    return str.count(texto,"...")+str.count(texto,"?")+str.count(texto,"!")+str.count(texto,". ")