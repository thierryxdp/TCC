def conta_frases(frase):
    '''funçao que conta o numero de frases dentro de uma frase, contando que termina as frases sendo (?, ., !,...). str->int'''
    ponto=str.count(frases'.')
    exclamacao=str.count(frases'!')
    interrogacao=str.count(frases'?')
    reticencias=str.count(frases'...')
    
    return ponto-3*reticencias+raticencias+interrogacao+exclamacao