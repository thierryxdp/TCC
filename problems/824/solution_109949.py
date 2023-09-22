def uppCons(frase):
    '''ok'''
    letra=frase.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','').replace('ã','')
    for frase in letra:
        return letra.upper()+frase