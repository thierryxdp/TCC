def uppCons(frase):
    
    """ Transforma as consoantes em maiúsculas"""
    
    frase_tratada = ''
    i=0
    while i <len(frase):
        caractere=frase[i]
        if caracatere in 'çbcdfghjklmnpqrstvwxyz':
            caractere=str.upper(caractere)
        frase_tratada=frase_tratada+caractere
        i=i+1
    return frase_tratada