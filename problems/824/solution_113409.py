def uppCons(frase):
    '''Recebe uma frase e retorna a mesma frase mas com todas as
    consoantes em maiúsculo
    str->str'''
    proximo=0
    novafrase=''
    while proximo<len(frase):
        letra=frase[proximo]
        if letra not in 'AEIOUaeiouáéíóúÁÉÍÓÚãõÃÕêôÊÔ':
            novafrase=novafrase+str.upper(letra)
        else:
            if letra in 'AEIOUaeiouáéíóúÁÉÍÓÚãõÃÕêôÊÔ':
            	novafrase=novafrase+letra
        proximo=proximo+1
    return novafrase