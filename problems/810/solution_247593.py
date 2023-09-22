def inverte(frase):
    frase= frase.lower()
    x= frase.replace('.',' ')
    x= x.replace('?','.')
    x= x.replace(',',' ') 
    x= x.replace('-',' ')
    x= x.replace('!',' ')
    x= x.split()
    return list.reverse(x)