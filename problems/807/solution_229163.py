def conta_frases(texto):
    '''conta o número de frases que aparecem em um dado texto, delimitadas pelo uso de um ponto final, um ponto de exclamação, um ponto de interogação ou reticências no final de cada frase
    str -> int'''
    reticencias = len(texto.split('...')) - 1
    interrogacao = len(texto.split('?')) - 1
    exclamacao = len(texto.split('!')) - 1
    ponto_final = (len(texto.split('.')) - 3 * reticencias) - 1
    return reticencias + interrogacao + exclamacao + ponto_final