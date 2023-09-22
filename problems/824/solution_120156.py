def uppCons(frase):
    cont=0
    frase_cons=''
    while cont<len(frase):
        if frase[cont]in'bcçdfghjlmnpqrstvxzBCÇDFGHJLMNPQRSTVXZ'
           frase_cons +=[frase[cont].upper()
        else:
           frase_cons +=frase_cons[cont]
           cont=cont+1
           return frase_cons