def uppCons(frase):
    filtro = ()
    i = 0
    while i < len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvxyz':
            filtro = filtro + (str.upper(frase[i])
        i = i + 1