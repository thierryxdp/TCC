def uppCons (frase):
    i=0
    final= ''
    while i < len(frase):
        if frase[i] in 'BCDBCDFGHJKLMNPQRSTVWXYZ':
            subir= str.upper (frase[i])
            final= final+subir
        i=i+1
    return final