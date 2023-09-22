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
    frase = str.split(frase)
    return frase[::-1]