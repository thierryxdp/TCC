def uppCons(frase):
    '''função que recebe uma frase e retorna a frase com todas as suas
    consoantes em maiúsculas; str-->str'''
    proximo=0
    str.split(frase)
    while proximo<len(frase):
        if frase[proximo] in 'bcdfghjklmnpqrstvwxyz':
            frase[proximo]=str.upper(frase[proximo])
        proximo=proximo+1
    str.join(' ',frase)
    return frase