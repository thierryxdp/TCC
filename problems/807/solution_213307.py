def conta_frases (x):
    '''Função que recebe um texto e conta o numero de frases
    presentes neste texto
    string->int'''
    x=str.replace(x,'...','!')
    return str.count(x,'.') + str.count(x,'!') + str.count(x,'?') + str.count(x'...')