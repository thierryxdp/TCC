def uppCons(frase):
    ''' funcao que recebe uma frase e a retorna com todas as consoantes maiusculas'''
    i = 1
    if(frase [0] in 'aeiouAEIOU'
       modifica = frase[0]
    else:
        modifica  =  str.upper(frase[0])
    while(i < len(frase)):
        if(frase[i] in b'cdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRTVWXYZ'):
            frase = str.upper(frase)
            modificada = modificada + frase[i]
        else:
            frase = str.lower(frase)
            modificada = modificada + frase[i]
        i += 1
    return modificada