def uppCons(x):
    maiuscula = ''
    caractere = 0
    consoante = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
    while caractere<len(x):
        if x[caractere] in consoante:
            maiuscula = maiuscula + str.upper(x[caractere])
        else:
            maiuscula = maiuscula + x[caractere]
        caractere = caractere + 1
    return maiuscula