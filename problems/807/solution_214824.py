def conta_frases(texto):
    '''Função que calcula e retorna o número de frases presentes no texto de
    entrada. A cada ponto final (!,?,.,...) é considerada uma frase.
    OBS: não pode colocar mais de um ponto final em sequência. ex.:????
    str -> int'''
    q1 = str.count(texto,'!')
    q2 = str.count(texto,'?')
    q3 = str.count(texto,'.')
    q4 = str.count(texto,'...')
    return q1 + q2 + q3 - 2*q4