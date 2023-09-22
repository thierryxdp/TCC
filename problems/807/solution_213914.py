def conta_frases(texto):
    '''Função que dado um texto contido em uma string, retorna a quantidade de frases que esse
    texto possui.
    string -> int'''
    reticencias = texto.count('...')
    ponto = texto.count('.') - reticencias*3
    return texto.count('!') + texto.count('?') + reticencias + ponto