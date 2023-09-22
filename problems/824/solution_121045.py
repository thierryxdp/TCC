def uppCons(frase):
    string = ''
    x=0
    while x<len(frase):
        if frase[x] in 'bcçdfghjklmnpqrstvwxyz':
            string+=frase[x].upper()
        else:
            string+=frase[x]
        x+=1
    return string