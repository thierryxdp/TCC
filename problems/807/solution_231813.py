def conta_frases(texto):
    '''calcula e retorna o número de frases que aparece no texto;
    str->int'''
    interrog=str.count(texto,'?')
    exclam=str.count(texto,'!')
    retic=str.count(texto,'...')
    ponto=str.count(texto,'.')
    
    return interrog+exclam+(-3*retic)+ponto