def conta_frases(frases):
    '''funcao que recebe frases em uma string e retorna o numero de frases separadas por pontos de
    conclusao como ponto final, exclamacao, etc. entrada: str; saida: int'''
    str.split(frases,'...')