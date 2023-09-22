def uppCons (frase):
    i=0
    final= ''
    while i < len(frase):
        if frase[i] in 'BCDBCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvxwyz':
            subir= str.upper (frase[i])
            final= final+subir+frase
        i=i+1
    return final