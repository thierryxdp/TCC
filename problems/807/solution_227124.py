def conta_frases(frases):
    '''funcao que recebe frases em uma string e retorna o numero de frases separadas por pontos de
    conclusao como ponto final, exclamacao, etc. entrada: str; saida: int'''
    frases1 = str.replace(frases,'...','.')
    frases2 = str.replace(frases1,'?','.')
    frases3 = str.replace(frases2,'!','.')
    return len(str.split(frases3,'.'))