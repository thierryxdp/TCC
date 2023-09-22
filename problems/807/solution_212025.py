def conta_frases (texto):
    '''função que retorna o número de frases em um texto. Uma frase é contabilizada em todo ponto final, exclamação
    interrogação ou reticências.
    string -> int'''
    reticencias = str.split(texto, '...')
    interrogacao = str.split(reticencias, '?')
    exclamacao = str.split(interrogacao, '!')
    ponto = str.split(exclamacao, '.')
    return len(ponto)