def uppCons(frase):
    ''' Essa função recebe uma frase e retorna a mesma com todas as consoantes em maiúsculas;
    str -> str. '''
    frase_nova= ''
    i=0
    while i < len(frase):
        cons=frase[i]
        if cons.lower() in 'bcdfghjklmnpqrstvz':
             cons=cons.upper()
        frase_nova += cons
        i+=1
    return frase_nova