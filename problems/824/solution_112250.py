def maiu(letra):
    ''' função que põe a consoante como maiúscula'''
    consoantes = ['q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f',
                  'g', 'h', 'j', 'k', 'l', 'ç', 'z', 'x', 'c',
                  'v', 'b', 'n', 'm']
    return str.upper(letra) if letra in consoantes else letra

def uppCons(frase):
    ''' põe as consoantes em maiúsculo'''

    fraseNew = str.join('', list(map(maiu, frase)))

    return fraseNew