def uppCons(frase):
    tam=len(frase)
    frase2=''
    cont=0
    
    while cont < tam:
        if frase[cont] in 'bcdfghjklmnpqrstvwxyzç':
            frase2 = frase2 + str.upper(frase[cont])
        else:
            frase2 = frase2 + frase[cont]
        cont = cont + 1
        
    return frase2