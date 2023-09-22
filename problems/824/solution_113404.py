def uppCons(frase):
    '''Recebe uma frase e retorna a mesma frase mas com todas as
    consoantes em maiúsculo
    str->str'''
    proximo=0
    novafrase=''
    while proximo<len(frase):
        if frase[proximo] not in 'AEIOUaeiou':
            novafrase=novafrase+str.lower(frase[proximo])
        else:
            if frase[proximo] in 'AEIOUaeiou':
            	novafrase=novafrase+frase[proximo]
        proximo=proximo+1
    return novafrase