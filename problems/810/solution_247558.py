def inverte(frase):
    x= frase.replace('.',' ')
    y= x.replace('?','.')
    z= y.replace(',',' ') 
    v= z.replace('-',' ')
    p= v.replace('!',' ')
    return p.reverte(p.lower())