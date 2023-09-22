def conta_frases(texto):
    '''funcao que recebe um texto e retorna o numero de frases que compoem esse texto
    str -> int'''
    terminacao=('.','!','?','...')
    if terminacao==terminacao[0] or terminacao==terminacao[1] or terminacao==terminacao[2] or terminacao==terminacao[3]:
        str.replace(texto,pontuacao,'#')
        return str.strip(texto,'#')