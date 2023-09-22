def conta_frases(texto):
    '''Função que retorna o número de frases em um texto, sejam eles 
    terminadas por ponto final, ponto de exclamação, inrerrogação, ou 
    reticências.     str => int'''
    frases = 0
    ''' 'frases' é um valor afetado por condições 'if' de acordo com a
    estrutura das frases da variável 'texto' . '''
    
    if '...' in texto:
        frases = frases+str.count(texto,'...')
    if '.' in texto:
        frases = frases+str.count(texto,'.')-3*str.count(texto,'...')
    if '?' in texto:
        frases = frases+str.count(texto,'?')
    if '!' in texto:
        frases = frases+str.count(texto,'!')
    return frases