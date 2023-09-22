def conta_frases(frases):
    '''funcao que recebe frases em uma string e retorna o numero de frases separadas por pontos de
    conclusao como ponto final, exclamacao, etc. entrada: str; saida: int'''
    frases1 = str.split(frases,'...')
    frases2 = str.split(frases,'?')
    frases3 = str.split(frases,'!')
    frases4 = str.split(frases,'.')
    frases5 = str.join(frases1, frases2, frases3, frases4,)
    return len(frases5)