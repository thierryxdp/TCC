def inverte(frase):
    '''função dado uma frase remove todas pontuações
    str--->str'''
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.lower(frase)
    frase = str.split(frase)
    frase= frase[::-1]
    return frase[1:-1]