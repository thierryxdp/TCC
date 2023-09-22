def conta_frases(frases):
    '''Funcao que retorna a quantidade de frases presentes no texto de entrada, sendo elas separadas por pontos, finais, de interrogaçao, de exclamacao ou reticencias.
    string -> int'''
    contar = str.count
    return contar(frases,'.')+contar(frases,'!')+contar(frases,'?')+contar(frases,'...')-3*contar(frases,'...')