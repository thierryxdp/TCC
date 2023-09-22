def inverte(frase):
    frase = str.replace(frase,'...','.')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,';',' ')
    frase = str.lower(frase)
    frase_l_inv = str.split(frase)[::-1]
    return str.join(' ',frase_l_inv)