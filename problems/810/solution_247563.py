def inverte(frase):
    frase= frase.lower()
    x= frase.replace('.',' ')
    y= x.replace('?','.')
    z= y.replace(',',' ') 
    v= z.replace('-',' ')
    final= v.replace('!',' ')
    return