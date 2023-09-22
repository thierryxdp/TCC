def conta_frases(frase):
    '''função que retorna
    entrada: string
    saída: int'''
    
    return str.count(frase, '.') + str.count(frase, '...') + str.count(frase,'?') + str.count(frase, '!') - str.count(frase, ',')