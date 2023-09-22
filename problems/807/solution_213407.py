def conta_frases(texto):
    '''conta o numero de frases presentes em um texto, as quais sao delimitadas por ponto de exclamaçao, final, de interrogaçao ou reticencias
    parameters:
    texto: um texto qualquer
   str->int'''
    return str.count(texto,'.') + str.count(texto,'!') + str.count(texto,'?') - 2 * str.count(texto,'...')