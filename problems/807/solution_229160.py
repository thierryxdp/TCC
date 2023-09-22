def conta_frases(texto):
    '''conta o número de frases que aparecem em um dado texto, delimitadas pelo uso de um ponto final, um ponto de exclamação, um ponto de interogação ou reticências no final de cada frase
    str -> int'''
    conta_frases1 = texto.split('...')
    conta_frases2 = conta_frases1.split('!')
    conta_frases3 = conta_frases2.split('?')
    conta_frases4 = conta_frases3.split('.')
    return len(conta_frases4)