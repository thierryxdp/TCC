def uppCons(frase):
    '''função que recebe uma frase e retorna a frase com todas as suas
    consoantes em maiúsculas; str-->str'''
    proximo=0
    frase_cons=''
    while proximo<len(frase):
        if frase[proximo] in 'bcdfghjklmnpqrstvwxyz':
            frase_cons=frase_cons+str.upper(frase[proximo])
        frase_cons=frase_cons+frase[proximo]
        proximo=proximo+1
    return frase_cons