def conta_frases(texto):
    '''funcao que recebe um texto e retorna o numero de frases que compoem esse texto
    str -> int'''
    terminacao=('.','!','?','...')
    if terminacao==terminacao[0]:
        str.replace(texto,terminacao,'#')
    if terminacao==terminacao[1]:
        str.replace(texto,terminacao,'#')
    if terminacao==terminacao[2]:
        str.replace(texto,terminacao,'#')
    if terminacao==terminacao[3]:
        str.replace(texto,terminacao,'#')
        return len(str.split(texto,'#'))