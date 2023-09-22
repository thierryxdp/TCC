def uppCons(frase):
    '''Funcao que, dada uma frase, retorna a mesma frase com todas as consoantes em maiúsculo; str -> str'''
    proxima=0
    novafrase=''
    while proxima<len(frase):
        if frase[proxima] in 'bcdfghjklmnpqrstvxywzç':
            novafrase+=frase[proxima].upper()
        else:
            novafrase+=frase[proxima]
        proxima=proxima+1
    return novafrase