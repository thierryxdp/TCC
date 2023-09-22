def conta_frases (texto):
    '''
    funcao que recebe um texto e retorna o numero de frases que aparecem nele
    str -> int
    '''
    tipo_exclamacao = str.replace(texto, ('!'), '.')
    tipo_sequencia = str.replace(tipo_exclamacao, ('...'), '.')
    tipo_interrogativa =str.replace(tipo_sequencia, ('?'), '.')
    return str.count (tipo_interrogativa,".")