def conta_frases (texto):
    """Função que, dado um texto, retorna seu número de frases
    entrada: string
    saída: int"""
    ponto_final=str.count(texto,'.')
    exclama=str.count(texto,'!')
    interrog=str.count(texto,'?')
    reticencias=str.count(texto,'...')
    if '.' and '...' in texto:
        return exclama+interrog+((ponto_final+reticencias)//2)
    else:
        return ponto_final+exclama+interrog+reticencias