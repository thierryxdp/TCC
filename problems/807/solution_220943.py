def conta_frases(texto):
    '''funçao que retorna a quantidade de frases de um dado texto;
    str -> str'''
    frases=texto
    separacao=(frases.split('[.!?]', frases))
    quantidade=len(separacao)
    return quantidade