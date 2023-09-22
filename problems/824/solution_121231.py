def uppCons(frase):
    '''Ao reber uma frase como argumento retorna
todas as consoantes em maisculas e nao altera as demais.'''
    i = 0
    while i < len(frase):
        if frase[i] not in 'aeiouAEIOU':
            x = frase.replace(frase[i], frase[i].upper())
        i = i +1
    return xdef uppCons(frase):
    '''Ao reber uma frase como argumento retorna
todas as consoantes em maisculas e nao altera as demais.'''
    i = 0
    while i < len(frase):
        if frase[i] not in 'aeiouAEIOU':
            x = frase.replace(frase[i], frase[i].upper())
        i = i +1
    return x