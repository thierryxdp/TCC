def conta_frases(string):
    '''Conta o número de frases em um texto(frases
       terminadas em '.', '!', '?', '...');
       str -> int'''
    return str.count(string,'.') + str.count(string, '!') + str.count(string, '?') + str.count(string, '...') - 3*str.count(string, '...')