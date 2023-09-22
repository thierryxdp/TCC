def conta_frases(texto):
    '''funçao que retorna a quantidade de frases de um dado texto;
    str -> str'''
    frases=texto
    separacao=(frases.split('[.!?]', texto))
    quantidade=len(separacao)
    return quantidade