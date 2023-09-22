def funcao_frases(frases):
    '''retorna o numero de frases de acordo com o numero de pontuacoes
    str->int'''
    return len(frases.split('.','!','?','...'))