def uppCons(frase):
    '''Retorna a frase original com todas
       as consoantes maiúsculas;str->str'''
    i=0
    frase=str.lower(frase)
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
           frase=str.replace(frase,frase[i],frase[i].upper())
        i=i+1
    return frase