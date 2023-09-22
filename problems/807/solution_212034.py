def conta_frases (texto):
    '''função que retorna o número de frases em um texto. Uma frase é contabilizada em todo ponto final, exclamação
    interrogação ou reticências.
    string -> int'''
    reticencias = str.replace(texto, '...', 'fim da frase')
    interrogacao = str.replace(reticencias, '?', 'fim da frase')
    exclamacao = str.replace(interrogacao, '!', 'fim da frase')
    ponto = str.replace(exclamacao, '.', 'fim da frase')
    return len(str.split(ponto, 'fim da frase'))