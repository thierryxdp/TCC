def conta_frases(texto):
    '''
       Dado um texto a função retorna quantas frases estão
       presentes nesse texto baseado nos pontos de conclusão
       no final de cada frase
       str -> int
    '''
    if '.' in texto:
        final = str.count(texto, '.')
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
    total = final + exclamacao + interrogacao + reticencias
    return total
    elif '.' and '...' in texto:
        total = (final + exclamacao + interrogacao + reticencias) - 3*final
        return total