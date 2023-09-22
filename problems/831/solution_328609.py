def lingua_p (frase):
    '''str->str'''
    p=''
    for x in frase:
        if x in 'aeiouáàãâéêóôõ':
            p= p +x +'p'+ x
        elif x in 'bcdfghjklmnpqrstvwxyzç':
            p= p + x
    
    return str.lower(p)