def uppCons(frase):
    '''Retorna a frase original com todas
       as consoantes maiúsculas;str->str'''
    i=0
    while i<len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVXWYZbcdfghjklmnpqrstvxwyz':
           frase=str.replace(frase,frase[i],frase[i].upper())
        i=i+1
    return frase