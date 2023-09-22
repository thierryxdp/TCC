def uppCons(frase):
    '''Altera uma frase dada para que todas as consoantes fiquem maiúsculas
    str --> str'''
    i = 0
    aux = ''
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyzç':
            aux += frase[i].upper()
        else:
            aux += frase[i]
        i += 12
    return aux