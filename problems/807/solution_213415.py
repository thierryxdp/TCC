def conta_frases(frase):
    '''coment'''
    subst1= str.replace(frase,'...','!')
    subst2= str.replace(subst1,'.','!')
    f1= str.count(subst2,'!')
    f2= str.count(frase,'.')
    returnf1