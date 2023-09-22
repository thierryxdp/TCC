def conta_frases(texto):
    '''conta o número de frases que aparecem em um dado texto, delimitadas pelo uso de um ponto final, um ponto de exclamação, um ponto de interogação ou reticências no final de cada frase
    str -> int'''
    contador = 0
    conta_frases1 = texto.split('...')
    while contador < len(conta_frases1):
    	conta_frases2 = conta_frases1[contador].split('!')
        contador += 1
    contador = 0
    while contador < len(conta_frases2):
    	conta_frases3 = conta_frases2[contador].split('?')
        contador += 1
    contador = 0
    while contador < len(conta_frases3):
    	conta_frases4 = conta_frases3[contador].split('.')
        contador += 1
    return len(conta_frases4) - 1