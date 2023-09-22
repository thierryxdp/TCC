def conta_frases(texto):
    '''Dada um texto, retornará a quantidade de frase presentes nele terminadas
    por ( .,!,?,...). (str=>int)'''

    f = 0
    
    if '!' in texto:
        f = f + str.count(texto, '!')
        

    if '?' in texto:
        f = f + str.count(texto,'?')


    if '...' in texto:
        texto = str.replace(texto,'...','.')

    if '.' in texto:
        f = f + str.count(texto, '.')

    return f