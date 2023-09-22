def conta_frases(frase):
    '''funçao que conta o numero de frases dentro de uma frase, contando que termina as frases sendo (?, ., !,...). str->int'''
    ponto=str.count(frase,'.')
    exclamacao=str.count(frase,'!')
    interrogacao=str.count(frase,'?')
    reticencias=str.count(frase,'...')
    
    return ponto-3*reticencias+raticencias+interrogacao+exclamacao