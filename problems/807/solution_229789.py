def conta_frases(texto):
    '''
       Dado um texto a função retorna quantas frases estão
       presentes nesse texto baseado nos pontos de conclusão
       no final de cada frase
       str -> int
    '''
    if '.' in texto:
        final = len(str.split('.'))
    if '!' in texto:
        exclamacao = len(str.split('!'))
    if '?' in texto:
        interrogacao = len(str.split('?')) 
    if '...' in texto:
        reticencias = len(str.split ('...'))
    return final + exclamacao + interrogacao + reticencias