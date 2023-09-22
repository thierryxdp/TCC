def uppCons(frase):
    '''Funcao que, dada uma frase, retorna a mesma frase com todas as consoantes em maiúsculo; str -> str'''
    proxima=0
    novafrase=''
    while proxima<len(frase):
        if frase[proxima] in 'bcdfghjklmnpqrstvxywz':
            novafrase=str.upper(frase[proxima])
        else:
            novafrase=frase[proxima]
        proxima=proxima+1
    return novafrase