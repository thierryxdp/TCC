def conta_frases (frases):
    '''recebe uma string, calcula e retorna o número de frases contidas nela'''
    '''string->int'''
    ponto = str.count (frases, '.')
    interrogacao = str.count (frases, '?')
    exclamacao = str.count (frases, '!')
    reticencias = str.count (frases, '...')
    final = ponto + interrogacao + exclamacao + reticencias
    
    if reticencias >=1:
        return final - reticencias*3
    else:
        return final