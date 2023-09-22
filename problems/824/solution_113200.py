#
#
#
#
def uppCons(frase):
    i=0
    nova_frase=''
    while i < len(frase):
        if not frase[i] in 'AEIOUaeiouÁÀÃÉÍÓÕÚáàãéíóõú':
            u=str.upper(frase[i])            
        i=i+1
    return nova_frase