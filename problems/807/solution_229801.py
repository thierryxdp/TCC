def conta_frases(texto):
    '''
       Dado um texto a função retorna quantas frases estão
       presentes nesse texto baseado nos pontos de conclusão
       no final de cada frase
       str -> int
    '''
    if '.' in texto:
        final = len(str.split('.'))
    if '.' not in texto:
        final = 0
    if '!' in texto:
        exclamacao = str.count(texto, '!')
    if '!' not in texto:
        exclamacao = 0
    if '?' in texto:
        interrogacao = str.count(texto, '?')
    if '?' not in texto:
        interrogacao = 0
    if '...' in texto:
        reticencias = str.count(texto, '...')
    if '...' not in texto:
        reticencias = 0
    return final + exclamacao + interrogacao + reticencias