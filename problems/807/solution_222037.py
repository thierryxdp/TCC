def conta_frases(texto):
    '''funcao que recebe um texto e retorna o numero de frases que compoem esse texto
    str -> int'''
    terminacao=('.','!','?','...')
    if terminacao==terminacao[0] or terminacao==terminacao[1] or terminacao==terminacao[2] or terminacao==terminacao[3]:
        frases=str.replace(texto,pontuacao,'#')
        lista_frases=str.split(frases,'#')
        return len(lista_frases)