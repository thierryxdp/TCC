def conta_frases(frases,pontuacoes):
    '''recebe uma string contendo texto e retrna em inteiros quantas frases tem esse texto'''
    pontuacoes=('.,!,?,:,;,...,')
    return len(str.split(frases,pontuacoes,)