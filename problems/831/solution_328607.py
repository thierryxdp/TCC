def lingua_p (frase):
    '''str->str'''
    p=''
    i=0
    while i < len(frase):
        for x in frase:
            if x in 'aeiouáàãâéêóôõ':
                p= p + x
            elif x in 'bcdfghjklmnpqrstvwxyzç':
                p= p + x + p[i-1]
        i= i+1
    
    return str.lower(p)