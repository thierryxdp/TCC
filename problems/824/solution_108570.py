def uppCons(frase):
    '''  '''
    indice = 0
    indiceCons = 0
    consoantes = 'bcçdfghjklmnpqrstvwxyz'
    
    while indice < len(frase) and indiceCons < len(consoantes):
        if consoantes[indiceCons] in frase:
            consoanteFrase = frase[frase.index(consoantes[indiceCons])]
            frase = frase.replace(consoanteFrase,consoanteFrase.upper())
        indiceCons += 1
        indice +=1
    return frase