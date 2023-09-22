def uppCons(frase):
    nova_frase=''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxywz':
              nova_frase=nova_frase + str.upper(frase[i])
        else:
            nova_frase = nova_frase + frase[i]
        i=i+1
    return nova_frase