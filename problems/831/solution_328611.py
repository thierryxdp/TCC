def lingua_p (frase):
    '''Dada um frase a função 'traduz' e a retorna na
    lingua do p;
    str->str'''
    p=''
    for x in frase:
        if x in 'aeiouáàãâéêóôõú':
            p= p +x +'p'+ x
        elif x in 'bcdfghjklmnpqrstvwxyzç':
            p= p + x
    
    return str.lower(p)