def uppCons (frase):
    i=0
    final= ''
    while i < len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvxwyz':
            subir= str.upper (frase[i])
            rep= str.replace(frase,frase,subir)
            final= rep
        i=i+1
    return final