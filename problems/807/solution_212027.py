def conta_frases (texto):
    '''função que retorna o número de frases em um texto. Uma frase é contabilizada em todo ponto final, exclamação
    interrogação ou reticências.
    string -> int'''
    reticencias = str.strip(texto, '...')
    interrogacao = str.strip(reticencias, '?')
    exclamacao = str.strip(interrogacao, '!')
    ponto = str.strip(exclamacao, '.')
    return len(str.split(ponto))