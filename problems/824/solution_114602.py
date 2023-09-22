def uppCons(frase):
    '''Funcao que, dada uma frase, retorna a mesma frase com todas as consoantes em maiúsculo; str -> str'''
    frase=str.split(frase)
    proxima=0
    while proxima<len(frase):
        if frase[proxima] in 'bcdfghjklmnpqrstvxywz':
            novafrase=str.replace(frase,proxima,str.upper(proxima))
    proxima=proxima+1
    return str.join(novafrase,',')