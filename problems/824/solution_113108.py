def uppCons (frase):
    i=0
    final= ''
    while i < len(frase):
        if frase[i] in 'BCDBCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvxwyz':
            subir= str.upper (frase[i])
        i=i+1
    return final