def uppCons(frase):
    nova_frase = 0
    i = 0 
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            nova_frase = nova_frase + frase[i].upper()
        else:
            nova_frase = nova_frase + frase[i]
        i=i+1
    return nova_frase