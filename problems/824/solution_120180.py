def uppCons(frase):
    cont=0
    frase_cons=''
    while cont<len(frase):
        if frase[cont]in"bcçdfghjlmnpqrstvxz":
            str.upper(frase[cont])
            cont=cont+1
            return frase_cons
 print(uppCons "viva a vida")