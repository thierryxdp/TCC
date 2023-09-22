def uppCons(frase):
    '''Recebe uma frase e retorna deixa todas as consoantes em letra maiscula
    str-->str'''
    s = ''
    for consoante in frase:
        if consoante in 'bcdfghjklmnpqrstvxwyz':
            s = s + consoante.upper() 
        else: 
            s = s + consoante
    return s