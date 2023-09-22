def conta_frases(texto):
    '''funçao que retorna a quantidade de frases de um dado texto;
    str -> str'''
    frases=texto
    separacao=(texto.split('.' or '!' or '?'))
    quantidade=len(separacao)-1
    return quantidade