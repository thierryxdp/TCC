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
            nova_frase=str.replace(nova_frase,frase[i],u)
        i=i+1
    return nova_frase