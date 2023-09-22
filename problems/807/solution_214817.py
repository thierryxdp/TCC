def conta_frases(texto):
    '''Função que calcula e retorna o número de frases presentes no texto de
    entrada. A cada ponto final (!,?,.,...) é considerada uma frase.
    OBS: não pode colocar mais de um ponto final em sequência. ex.:????
    str -> int'''
    for caractere in '!':
        q1 = str.count(texto,caractere)
    for caractere in '?':
        q2 = str.count(texto,caractere)
    for caractere in '.':
        q4 = str.count(texto,caractere)
        return q1 + q2 + q3 + q4