def conta_frases(frases):
    '''recebe uma string contendo texto e retorna em inteiros quantas frases tem dentro do texto texto'''
    pontuacoes=('.,!,?,:,;,...,')
    return len(str.split(frases,pontuacoes)