def uppCons(frase):
    '''ok'''
    letra=frase.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','').replace('ã','')
    for letra in frase:
        return letra.upper,frase