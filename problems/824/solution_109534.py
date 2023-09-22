def uppCons(frase):
    
    '''recebe uma frase e retorna a frase com todas suas consoantes maiúsculas, enquanto os demais caracteres continuam minúsculos.
    str -> str'''
    
    proximo = 0
    while proximo < len(frase):
        if frase[proximo] in 'bcçdfghjklmnpqrstvwxyz':
            frase = str.replace(frase,frase[proximo],str.upper(frase[proximo]))
        proximo = proximo + 1
    return frase