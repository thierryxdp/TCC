def conta_frases(texto):
    '''Função que retorna o número de frases que compõem o texto
texto=string->int'''
    return len(texto.join('.''!''?''...',texto.split()))