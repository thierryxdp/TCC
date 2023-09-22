def conta_frases(texto):
    'função que recebe um texto e retorna a quantidade de frases contidas nele'
    ponto = texto.count('.')-3*texto.count('...')
    exclamacao = texto.count('!')
    interrogacao = texto.count('?')
    reticencias = texto.count('...')
    return ponto+exclamacao+interrogacao+reticencias