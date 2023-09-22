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
    frase= str(frase[::-1])
    frase= str.replace(frase,"', '", ' ')
    return frase[2:-2]