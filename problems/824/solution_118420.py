def uppCons(frase):
    '''comentario qualquer'''
   
    i=0
    while i<len(frase):
        if frase[i] in 'BCDFGHJKLMNOPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            frase=str.upper(frase[i])
            i = i+1
            return frase