#
#
#
#
def uppCons(frase):
    i=0
    nova_frase=frase
    while i < len(frase):
        if not frase[i] in 'AEIOUaeiouÁÀÃÉÍÓÕÚáàãéíóõú':
            u=str.upper(frase[i])
            str.insert(u,frase[i])
        i=i+1
    return nova_frase