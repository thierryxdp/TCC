def conta_frases(texto):
    '''funçao que retorna a quantidade de frases de um dado texto;
    str -> str'''
    
    frases=texto
    import re
    separacao=re.split('[.!?...]', texto)
    quantidade=len(separacao)
    return quantidade