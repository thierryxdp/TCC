def inverte(frase):
    frase= frase.lower()
    x= frase.replace('.',' ')
    x= x.replace('?','.')
    x= x.replace(',',' ') 
    x= x.replace('-',' ')
    x= x.replace('!',' ')
    final= x.split()
    return final.reverse()