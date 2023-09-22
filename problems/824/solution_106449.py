def uppCons(frase):
    '''recebe uma frase e a retorna com consoantes em letra maiuscula
    str->str'''
    palavras=str.split(frase)
    proximo=0
    while proximo<len(palavras):
        if 'bcdfghjklmnpqrstvwxyz' in palavras[proximo] 
            str.upper('bcdfghjklmnpqrstvwxyz')
        proximo=proximo+1
    return str.join(palavras,' ')