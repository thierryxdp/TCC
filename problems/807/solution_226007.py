def conta_frases(texto):
    '''Calcula a quantidade de frases tem em um texto; string->int'''
    import re
    return len(re.split("[,!?...]",texto)