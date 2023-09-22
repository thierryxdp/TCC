def uppCons(frase):
    '''Recebe uma frase e retorna a mesma frase com todas as consonantes em maiúsculas'''
    proximo=0
    while proximo<len(frase):
        if frase[proximo] not in 'AEIOUaeiou':
            str.replace(frase,frase[proximo],str.upper(frase[proximo])
        proximo=proximo+1
    return frase