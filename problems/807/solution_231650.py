def conta_frases(frases):
    '''Código que conta o número de frases em um dado texto
    str -> int'''
    final = frases.replace("...", 'teste')
    interrogacao = final.replace("!", 'teste')
    exclamacao = interrogacao.replace("?", 'teste')
    reticencia = exclamacao.replace(".", 'teste')
    return reticencia.count('teste')