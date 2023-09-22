def conta_frases(frase):
    '''coment'''
    subst1= str.replace(frase,'...','!')
    subst2= str.replace(subst1,'.','!')
    subst3= str.replace(subst2,'?','!')
    f1= str.count(subst3,'!')
    f2= str.count(frase,'.')
    return f1