uppCons(x):
    maiuscula = ''
    caractere = 0
    consoante = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
    while caractere<len(frase):
        if frase[caractere] in consoante:
            	maiuscula = maiuscula + str.upper(frase[caractere])
        else:
            	maiuscula = maiuscula + frase[caractere]
        caractere = caractere + 1
    return maiuscula