def uppCons (frase):
    '''Retorna a frase dada com todas as consoantes maiúsculas.
    str -> str'''
    proximo = 0
    while proximo<len(frase):
        if frase[proximo] in 'bcdfghjklmnpqrstvwxyz':
            frase=str.replace(frase,frase[proximo],str.upper(frase[proximo]))
        proximo = proximo +1
    return frase