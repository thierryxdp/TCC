def uppCons(frase):
    indice=0
    frase1=''.join(frase)
    frase2=list(frase1)
    while indice<len(frase2):
        if frase2[indice] in 'BCDFGHJKLMNPQRSTVXYZbcdfghjklmnpqrstvxyz':
            frase3=str.upper(frase[indice])
        indice=indice+1
        frase4=''.join(frase3)
    return str.split(frase4,',')