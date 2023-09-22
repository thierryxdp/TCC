def conta_frases (frase):
    '''função que retorna o número de frases que aparecem
    dentro de um texto'''
    '''str -> int'''
    ponto = frase.count('.')
    exclamacao = frase.count('!')
    interrogacao = frase.count('?')