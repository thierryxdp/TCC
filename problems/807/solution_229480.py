def conta_frases(texto):
    '''
    Funçao que recebe um texto e conta o numero de frases que
    aparecem dentro dele, levando em consideraçao a pontuaçao
    str -> int
    '''
    tamanho=str.split(texto,'!')
    return len(tamanho)