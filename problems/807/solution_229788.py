def conta_frases(texto):
    '''
       Dado um texto a função retorna quantas frases estão
       presentes nesse texto baseado nos pontos de conclusão
       no final de cada frase
       str -> int
    '''
    if '.' in frase:
        final = len(str.split('.'))
    if '!' in frase:
        exclamacao = len(str.split('!'))
    if '?' in frase:
        interrogacao = len(str.split('?')) 
    if '...' in frase:
        reticencias = len(str.split ('...'))
    return final + exclamacao + interrogacao + reticencias