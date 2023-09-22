def conta_frases(frase):
    '''funçao que conta o numero de frases dentro de uma frase, contando que termina as frases sendo (?, ., !,...). str->int'''
    frase= frase.strip()
    return len(frase)