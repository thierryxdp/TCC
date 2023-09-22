def uppCons(frase):
    nova_frase = 0
    i = 0 
    while i<len(frase):
        if frase[i] not in 'AEIOUÃÁÂÉÍÓÕÚaeiouãáâéíóõú':
            nova_frase = str(nova_frase) + frase[i].upper()
        else:
            nova_frase = str(nova_frase) + frase[i]
        i=i+1
    return nova_frase[1::]