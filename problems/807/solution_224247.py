def conta_frases (frases):
    '''Retorna a quantidade de frases presentes
    na string de entrada 'frases'
    str --> int'''
    ponto = str.count(frases, '.')
    interrogacao = str.count(frases, '?')
    exclamacao = str.count(frases, '!')
    reticencias = str.count(frases, '...')
        
    if '...' not in frases:
        return ponto + interrogacao + exclamacao
    else:
        return (ponto - (reticencias)*3) + interrogacao +  exclamacao + reticencias